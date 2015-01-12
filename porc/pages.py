from .resource import Resource
from collections import Iterator
import copy
try:
    # python 2
    from urllib import quote
except ImportError:
    # python 3
    from urllib.parse import quote


class Pages(Iterator):

    def __init__(self, opts, url, path, params):
        if isinstance(path, list):
            pages_url = '/'.join([url] + [quote(elem) for elem in path])
        else:
            pages_url = '/'.join([url, quote(path)])
        self.resource = Resource(pages_url, **opts)
        self.params = params
        self._root_resource = Resource(url[:url.find('/v0')], **opts)
        self.response = None

    def _handle_page(self, querydict={}, val='next', **headers):
        """
        Executes the request getting the next (or previous) page,
        incrementing (or decrementing) the current page.
        """
        params = copy.copy(self.params)
        params.update(querydict)
        # update uri based on next page
        if self.response:
            self.response.raise_for_status()
            _next = self.response.links.get(val, {}).get('url')
            if _next:
                response = self._root_resource._make_request(
                    'GET', _next, params, **headers)
                self._handle_res(None, response)
                return response
            else:
                raise StopIteration
        else:
            response = self.resource._make_request(
                'GET', '', params, **headers)
            self._handle_res(None, response)
            return response

    def _handle_res(self, session, response):
        """
        Stores the response, which we use for determining
        next and prev pages.
        """
        self.response = response

    def reset(self):
        """
        Clear the page's current place.

            page_1 = page.next().result()
            page_2 = page.next().result()
            page.reset()
            page_x = page.next().result()
            assert page_x.url == page_1.url
        """
        self.response = None

    def next(self, querydict={}, **headers):
        """
        Gets the next page of results.
        Raises `StopIteration` when there are no more results.
        """
        return self._handle_page(querydict, **headers)

    def __next__(self):
        return self.next()

    def prev(self, querydict={}, **headers):
        """
        Gets the previous page of results.
        Raises `StopIteration` when there are no more results.

        Note: Only collection searches provide a `prev` value.
        For all others, `prev` will always return `StopIteration`.
        """
        return self._handle_page(querydict, 'prev', **headers)

    def all(self):
        results = []
        for response in self:
          response.raise_for_status()
          results.extend(response['results'])
        return results

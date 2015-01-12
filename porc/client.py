from datetime import datetime
from .resource import Resource
from .version import VERSION
from .pages import Pages
from .patch import Patch
from . import util


class Client(Resource):

    def __init__(self, api_key, custom_url=None, use_async=False, **kwargs):
        self.api_key = api_key
        self.url = custom_url or 'https://api.orchestrate.io/v0'
        if 'headers' not in kwargs:
            kwargs['headers'] = {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'User-Agent': 'python-requests/1.2.0 porc/%s' % VERSION
            }
        kwargs['auth'] = (self.api_key, '')
        super(Client, self).__init__(self.url, use_async, **kwargs)

    def ping(self):
        return self._make_request('HEAD')

    def head(self, collection=None, key=None, ref=None):
        path = list()
        if collection:
            path.append(collection)
            if key:
                path.append(key)
                if ref:
                    path.append('refs')
                    path.append(ref)
        return self._make_request('HEAD', path)

    def get(self, collection, key, ref=None):
        if ref:
            path = [collection, key, 'refs', ref]
        else:
            path = [collection, key]
        return self._make_request('GET', path)

    def post(self, collection, body):
        return self._make_request('POST', collection, body)

    def put(self, collection, key, body, ref=None):
        opts = dict()
        if ref:
            opts['If-Match'] = ref.center(len(ref) + 2, '"')
        elif ref == False:
            opts['If-None-Match'] = '"*"'
        return self._make_request('PUT', [collection, key], body, opts)

    def patch(self, collection, key, body_or_patch, ref=None):
        opts = {'Content-Type': 'application/json-patch+json'}
        if type(ref) == str:
            opts['If-Match'] = '"' + ref + '"'
        elif ref == False:
            # If-None-Match is not relevant for a PATCH request.
            opts['If-None-Match'] = '"*"'

        if isinstance(body_or_patch, Patch):
            body = body_or_patch.operations
        else:
            body = body_or_patch

        return self._make_request('PATCH', [collection, key], body, opts)

    def patch_merge(self, collection, key, body, ref=None):
        opts = {'Content-Type': 'application/merge-patch+json'}
        if type(ref) == str:
            opts['If-Match'] = '"' + ref + '"'
        elif ref == False:
            # If-None-Match is not relevant for a PATCH request.
            opts['If-None-Match'] = '"*"'

        return self._make_request('PATCH', [collection, key], body, opts)

    def delete(self, collection, key=None, ref=None):
        if key:
            opts = dict()
            params = dict()
            if ref:
                opts['If-Match'] = ref.center(len(ref) + 2, '"')
            else:
                params['purge'] = True
            return self._make_request('DELETE', [collection, key], params, opts)
        else:
            return self._make_request('DELETE', collection, dict(force=True))

    def refs(self, collection, key, **params):
        return self._make_request('GET', [collection, key, 'refs'], params)

    def list(self, collection, **params):
        return Pages(self.opts, self.uri, collection, params)

    def search(self, collection, query, **params):
        params['query'] = query
        return Pages(self.opts, self.uri, collection, params)

    def get_relations(self, collection, key, *relations):
        path = [collection, key, 'relations'] + list(relations)
        return self._make_request('GET', path)

    def put_relation(self, collection, key, relation, to_collection, to_key):
        path = [collection, key, 'relation', relation, to_collection, to_key]
        return self._make_request('PUT', path)

    def delete_relation(self, collection, key, relation, to_collection, to_key):
        path = [collection, key, 'relation', relation, to_collection, to_key]
        return self._make_request('DELETE', path, dict(purge=True))

    def get_event(self, collection, key, event_type, timestamp, ordinal):
        if isinstance(timestamp, datetime):
            timestamp = util.datetime_to_timestamp(timestamp)
        path = [collection, key, 'events', event_type, timestamp, ordinal]
        return self._make_request('GET', path)

    def post_event(self, collection, key, event_type, data, timestamp=None):
        path = [collection, key, 'events', event_type]
        if timestamp:
            if isinstance(timestamp, datetime):
                timestamp = util.datetime_to_timestamp(timestamp)
            path.append(timestamp)
        return self._make_request('POST', path, data)

    def put_event(self, collection, key, event_type, timestamp, ordinal, data, ref=None):
        if isinstance(timestamp, datetime):
            timestamp = util.datetime_to_timestamp(timestamp)
        path = [collection, key, 'events', event_type, timestamp, ordinal]
        headers = dict()
        if ref:
            headers['If-Match'] = ref.center(len(ref) + 2, '"')
        return self._make_request('PUT', path, data, headers=headers)

    def delete_event(self, collection, key, event_type, timestamp, ordinal, ref=None):
        if isinstance(timestamp, datetime):
            timestamp = util.datetime_to_timestamp(timestamp)
        path = [collection, key, 'events', event_type, timestamp, ordinal]
        headers = dict()
        params = dict(purge=True)
        if ref:
            headers['If-Match'] = ref.center(len(ref) + 2, '"')
        return self._make_request('DELETE', path, params, headers=headers)

    def list_events(self, collection, key, event_type, **params):
        path = [collection, key, 'events', event_type]
        for param in ['startEvent', 'afterEvent', 'beforeEvent', 'endEvent']:
            if param in params and isinstance(params[param], datetime):
                params[param] = util.datetime_to_timestamp(params[param])
        return Pages(self.opts, self.uri, path, params)

    def async(self):
        return Async(self.api_key, self.url, **self.opts)


class Async(Client):

    def __init__(self, api_key, url, **opts):
        super(Async, self).__init__(api_key, url, True, **opts)

    def __enter__(self):
        return self

    def __exit__(self, type, value, stacktrace):
        return True

from requests import Response as Requests_Response
from collections import MutableMapping
import re

URL_PATTERNS = [
    "/v0/(?P<collection>.+)/(?P<key>.+)/events/(?P<type>.+)/(?P<timestamp>\d+)/(?P<ordinal>\d+)",
    "/v0/(?P<collection>.+)/(?P<key>.+)/events/(?P<type>.+)/(?P<timestamp>\d+)",
    "/v0/(?P<collection>.+)/(?P<key>.+)/events/(?P<type>.+)",
    "/v0/(?P<collection>.+)/(?P<key>.+)/refs/(?P<ref>.+)",
    "/v0/(?P<collection>.+)/(?P<key>.+)/refs",
    "/v0/(?P<collection>.+)/(?P<key>.+)/relations/(?P<kind>.+)/(?P<to_collection>.+)/(?P<to_key>.+)",
    "/v0/(?P<collection>.+)/(?P<key>.+)/relations/(?P<kinds>.+)",
    "/v0/(?P<collection>.+)/(?P<key>.+)",
    "/v0/(?P<collection>.+)"
]


class Response(MutableMapping):

    def __init__(self, resp):
        self.response = resp
        if self.response.text:
            self.json = self.response.json()
        else:
            self.json = dict()
        self._set_path()

    def _set_path(self):
        # match the url
        path = self.response.url[self.response.url.find('/v0'):]
        for regex in URL_PATTERNS:
            location_match = re.match(regex, path)
            if location_match:
                for key, value in location_match.groupdict().items():
                    setattr(self, key, value)
                break
        # match headers
        for regex in URL_PATTERNS:
            # check location
            location_match = re.match(
                regex, self.response.headers.get('location', ''))
            # if not in location, try content-location
            if not location_match:
                location_match = re.match(
                    regex, self.response.headers.get('content-location', ''))
            # if a match was found in either place, attach it to self
            if location_match:
                for key, value in location_match.groupdict().items():
                    setattr(self, key, value)
                break
        # finally, try the etag
        etag_match = re.match(
            '"(?P<ref>.+)"', self.response.headers.get('etag', ''))
        if etag_match:
            for key, value in etag_match.groupdict().items():
                setattr(self, key, value)

    def __getattr__(self, name):
        return getattr(self.response, name)

    def __getitem__(self, key):
        return self.json.get(key)

    def __setitem__(self, key, value):
        self.json[key] = value

    def __delitem__(self, key):
        del self.json[key]

    def __iter__(self):
        return iter(self.json)

    def __len__(self):
        return len(self.json)

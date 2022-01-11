import flask as f

from ..app import rule
from ..app._endpoint import AppEndpoint
from ..app.benchmarks import RunMixin


class Robots(AppEndpoint, RunMixin):
    def get(self):
        response = f.Response(
            response="User-Agent: *\nDisallow: /compare/\n",
            status=200,
            mimetype="text/plain",
        )
        response.headers["Content-Type"] = "text/plain; charset=utf-8"
        return response


rule(
    "/robots.txt",
    view_func=Robots.as_view("robots"),
    methods=["GET"],
)
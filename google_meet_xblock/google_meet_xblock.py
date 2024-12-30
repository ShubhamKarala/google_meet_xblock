import pkg_resources
from xblock.core import XBlock
from xblock.fields import String, Scope
from xblock.fragment import Fragment


class GoogleMeetXBlock(XBlock):
    """
    An XBlock to embed Google Meet URLs.
    """
    meet_url = String(
        help="URL for Google Meet",
        default="",
        scope=Scope.content,
    )

    def student_view(self, context=None):
        """
        The primary view shown to students when taking a course.
        """
        html = self.render_template("templates/google_meet_xblock.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/main.css"))
        frag.add_javascript(self.resource_string("static/js/main.js"))
        frag.initialize_js('GoogleMeetXBlock')
        return frag

    def studio_view(self, context=None):
        """
        The view for instructors to configure the XBlock.
        """
        html = self.render_template("templates/google_meet_studio.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/main.css"))
        frag.add_javascript(self.resource_string("static/js/main.js"))
        frag.initialize_js('GoogleMeetXBlockStudio')
        return frag

    @XBlock.json_handler
    def save_meet_url(self, data, suffix=''):
        """
        Save the Google Meet URL.
        """
        self.meet_url = data.get('meet_url', '').strip()
        return {"meet_url": self.meet_url}

    def resource_string(self, path):
        """
        Get resources from the package.
        """
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def render_template(self, path):
        """
        Render an HTML file from the templates folder.
        """
        template = self.resource_string(path)
        return template

import zope.interface
import zope.component

from pmr2.app.factory import named_factory
from pmr2.app.annotation.interfaces import *
from pmr2.app.annotation.annotator import ExposureFileAnnotatorBase
from pmr2.app.annotation.annotator import ExposureFileEditableAnnotatorBase


class CMGuiViewerAnnotator(ExposureFileEditableAnnotatorBase):
    zope.interface.implements(IExposureFileAnnotator)
    title = u'CMGui Viewer'
    label = u'CMGui Viewer'

    def generate(self):
        return ()

CMGuiViewerAnnotatorFactory = named_factory(CMGuiViewerAnnotator)

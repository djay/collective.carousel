from zope.interface import Interface
from plone.app.portlets.interfaces import IColumn

class ICollectiveCarouselLayer(Interface):
    """ A layer specific to collective.carousel
    """
    
class ICarouselProvider(Interface):
    """ We should be able to mark objects that can be used in carousel with 
        the special marker. For now this marks Collections only.
    """

try:
    from collective.contentleadimage.interfaces import ILeadImageable
except:
    ILeadImageable = None
from Products.ATContentTypes.interface import IATContentType
from Products.ATContentTypes.interface import IATNewsItem

if ILeadImageable is not None:
    # Need to make sure we come up top
    class IATWithLeadImage(ILeadImageable, IATContentType):
        """ More specific interface """

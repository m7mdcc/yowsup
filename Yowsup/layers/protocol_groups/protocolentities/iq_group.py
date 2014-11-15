from Yowsup.structs import ProtocolEntity, ProtocolTreeNode
from Yowsup.layers.protocol_iq.protocolentities import IqProtocolEntity
class GroupIqProtocolEntity(IqProtocolEntity):
    '''
    <iq type="{{get | set?}}" id="{{id}}" xmlns="w:g", to={{group_jid}}">
    </iq>
    '''
    def __init__(self, to = None, _from  = None, _id = None, _type = None):
        super(GroupIqProtocolEntity, self).__init__("w:g", _id, _type, to = to, _from = _from)
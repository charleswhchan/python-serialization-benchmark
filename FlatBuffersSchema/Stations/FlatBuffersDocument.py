# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Stations

import flatbuffers

class FlatBuffersDocument(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsFlatBuffersDocument(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FlatBuffersDocument()
        x.Init(buf, n + offset)
        return x

    # FlatBuffersDocument
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # FlatBuffersDocument
    def Type(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # FlatBuffersDocument
    def Features(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .Features import Features
            obj = Features()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # FlatBuffersDocument
    def FeaturesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def FlatBuffersDocumentStart(builder): builder.StartObject(2)
def FlatBuffersDocumentAddType(builder, type): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(type), 0)
def FlatBuffersDocumentAddFeatures(builder, features): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(features), 0)
def FlatBuffersDocumentStartFeaturesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def FlatBuffersDocumentEnd(builder): return builder.EndObject()
# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Stations

import flatbuffers

class Properties(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsProperties(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Properties()
        x.Init(buf, n + offset)
        return x

    # Properties
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Properties
    def Description(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Properties
    def MarkerSymbol(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Properties
    def Title(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Properties
    def Url(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Properties
    def Lines(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # Properties
    def LinesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Properties
    def Address(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def PropertiesStart(builder): builder.StartObject(6)
def PropertiesAddDescription(builder, description): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(description), 0)
def PropertiesAddMarkerSymbol(builder, markerSymbol): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(markerSymbol), 0)
def PropertiesAddTitle(builder, title): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(title), 0)
def PropertiesAddUrl(builder, url): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(url), 0)
def PropertiesAddLines(builder, lines): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(lines), 0)
def PropertiesStartLinesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def PropertiesAddAddress(builder, address): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(address), 0)
def PropertiesEnd(builder): return builder.EndObject()
# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Stations

import flatbuffers

class Geometry(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsGeometry(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Geometry()
        x.Init(buf, n + offset)
        return x

    # Geometry
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Geometry
    def Type(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Geometry
    def Coordinates(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = o + self._tab.Pos
            from .Coordinates import Coordinates
            obj = Coordinates()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def GeometryStart(builder): builder.StartObject(2)
def GeometryAddType(builder, type): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(type), 0)
def GeometryAddCoordinates(builder, coordinates): builder.PrependStructSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(coordinates), 0)
def GeometryEnd(builder): return builder.EndObject()
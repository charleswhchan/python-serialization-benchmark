# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Stations

import flatbuffers

class Coordinates(object):
    __slots__ = ['_tab']

    # Coordinates
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Coordinates
    def Lat(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0))
    # Coordinates
    def Lon(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(4))

def CreateCoordinates(builder, lat, lon):
    builder.Prep(4, 8)
    builder.PrependFloat32(lon)
    builder.PrependFloat32(lat)
    return builder.Offset()

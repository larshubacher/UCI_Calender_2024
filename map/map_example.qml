import QtQuick 
import QtPositioning 
import QtLocation 
import QtQuick.Controls 

Item
{
id: root
visible: true

Plugin
{
    id: osmPlug
    name: "osm"
    
    PluginParameter
    {
        name: "osm.mapping.providersrepository.disabled"
        value: "true"
    }
    PluginParameter
    {
        name: "osm.mapping.providersrepository.address"
        value: "http://maps-redirect.qt.io/osm/5.6/"
    }
}

Map
{
    id: map
    anchors.fill: parent
    plugin: osmPlug
    center: QtPositioning.coordinate(59.91, 10.75) // Oslo
    zoomLevel: 3
    copyrightsVisible: false
    fieldOfView: 15
}
}

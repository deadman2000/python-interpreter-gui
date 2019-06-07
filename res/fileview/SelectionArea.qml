import QtQuick 2.12

MouseArea {
    anchors.fill: parent
    acceptedButtons: Qt.LeftButton
    propagateComposedEvents: true

    onPressed: {
        var p = symAt(mouse)
        if (p) {
            var address = pointToAddress(p)
            pressAddress = address
            cursor.offset = address
        } else {
            pressAddress = -1
            selection.reset()
        }
    }

    onDoubleClicked: {
        var p = symAt(mouse)
        if (p) {
            var address = pointToAddress(p)
            console.log(address)
        }
    }

    onPositionChanged: {
        if (!pressed) return
        if (mouse.x < 0 || mouse.x > width) return

        var p = symAt(mouse)
        if (!p) return

        var address = pointToAddress(p)
        selection.begin = Math.min(pressAddress, address)
        selection.end = Math.max(pressAddress, address)
    }
}

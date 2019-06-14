import QtQuick 2.12
import QtQuick.Controls 2.5
import QtQuick.Controls.Material 2.12
import QtQuick.Dialogs 1.2
import QtQml.Models 2.2
import "../docking"
import ".."

DockPanel {
    title: "Structure"

    CustomTree {
        id: tree
        anchors.fill: parent
        model: currentFile.document.structure
        onSelectedNodeChanged: currentFile.selectRange(selectedNode)
        onDoubleClicked: currentFile.focusRange(selectedNode.range)
    }
}

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QGuiApplication, QFont
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType
from PyQt5 import QtCore

# noinspection PyUnresolvedReferences
import resource_rc
from address_range import AddressRange
from area_style import AreaStyle
from file_document import FileDocument
from interpreter_model import InterpreterModel
from qmlglobal import QmlGlobal


def qt_message_handler(mode, context, message):
    message = message.replace('file:///', '')

    if mode == QtCore.QtInfoMsg:
        mode = 'INFO'
    elif mode == QtCore.QtWarningMsg:
        mode = 'WARNING'
    elif mode == QtCore.QtCriticalMsg:
        mode = 'CRITICAL'
    elif mode == QtCore.QtFatalMsg:
        mode = 'FATAL'
    else:
        mode = 'DEBUG'

    print('%s:%d  %s()' % (context.file.replace('file:///', ''), context.line, context.function))
    print('%s: %s\n' % (mode, message))


QtCore.qInstallMessageHandler(qt_message_handler)

if __name__ == '__main__':
    os.environ['QT_QUICK_CONTROLS_FALLBACK_STYLE'] = 'Material'

    app = QGuiApplication(sys.argv)

    font = QFont("Roboto")
    app.setFont(font)

    qmlRegisterType(InterpreterModel, 'ReverseEngi', 1, 0, 'InterpreterModel')
    qmlRegisterType(AddressRange, 'ReverseEngi', 1, 0, 'AddressRange')
    qmlRegisterType(FileDocument, 'ReverseEngi', 1, 0, 'FileDocument')
    qmlRegisterType(AreaStyle, 'ReverseEngi', 1, 0, 'AreaStyle')

    engine = QQmlApplicationEngine()
    g = QmlGlobal()
    engine.rootContext().setContextProperty("G", g)
    engine.load(QUrl("res/main.qml"))

    sys.exit(app.exec_())

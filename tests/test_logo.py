import logging
import asyncio
import pytest

from sanic.config import BASE_LOGO


def test_logo_base(app, caplog):
    server = app.create_server(debug=True)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop._stopping = False

    with caplog.at_level(logging.DEBUG):
        _server = loop.run_until_complete(server)

    _server.close()
    loop.run_until_complete(_server.wait_closed())
    app.stop()

    assert caplog.record_tuples[0] == ("sanic.root", logging.DEBUG, BASE_LOGO)


def test_logo_false(app, caplog):
    app.config.LOGO = False

    server = app.create_server(debug=True)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop._stopping = False

    with caplog.at_level(logging.DEBUG):
        _server = loop.run_until_complete(server)

    _server.close()
    loop.run_until_complete(_server.wait_closed())
    app.stop()

    assert caplog.record_tuples[0] == (
        "sanic.root",
        logging.INFO,
        "Goin' Fast @ http://127.0.0.1:8000",
    )


def test_logo_true(app, caplog):
    app.config.LOGO = True

    server = app.create_server(debug=True)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop._stopping = False

    with caplog.at_level(logging.DEBUG):
        _server = loop.run_until_complete(server)

    _server.close()
    loop.run_until_complete(_server.wait_closed())
    app.stop()

    assert caplog.record_tuples[0] == ("sanic.root", logging.DEBUG, BASE_LOGO)


def test_logo_custom(app, caplog):
    app.config.LOGO = "My Custom Logo"

    server = app.create_server(debug=True)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop._stopping = False

    with caplog.at_level(logging.DEBUG):
        _server = loop.run_until_complete(server)

    _server.close()
    loop.run_until_complete(_server.wait_closed())
    app.stop()

    assert caplog.record_tuples[0] == (
        "sanic.root",
        logging.DEBUG,
        "My Custom Logo",
    )

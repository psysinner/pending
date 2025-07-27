import asyncio
from unittest.mock import AsyncMock, MagicMock
import pytest
from plugins.commands import accept

from unittest.mock import patch

@pytest.mark.asyncio
@patch('plugins.commands.db')
@patch('plugins.commands.Client')
async def test_accept_command(mock_client, mock_db):
    # Mock client and message objects
    client = AsyncMock()
    message = MagicMock()
    message.chat.id = 12345
    message.from_user.id = 67890

    # Mock the reply message chain
    show_mock = AsyncMock()
    show_mock.edit.return_value = show_mock
    message.reply.return_value = asyncio.Future()
    message.reply.return_value.set_result(show_mock)

    # Mock database and session
    mock_db.get_session.return_value = asyncio.Future()
    mock_db.get_session.return_value.set_result("test_session")

    # Mock the client created within the function
    acc_client_mock = AsyncMock()
    mock_client.return_value = acc_client_mock

    # Mock the listen functionality
    vj_mock = AsyncMock()
    vj_mock.forward_from_chat.id = 98765
    vj_mock.forward_from_chat.type = "channel"
    client.listen = AsyncMock(return_value=vj_mock)

    # Mock get_chat to avoid raising an exception
    acc_client_mock.get_chat.return_value = asyncio.Future()
    acc_client_mock.get_chat.return_value.set_result(None)

    await accept(client, message)

    # Assert that the initial reply was sent
    message.reply.assert_called_with("**Please Wait.....**")

    # Assert that the session was retrieved from the database
    mock_db.get_session.assert_called_with(67890)

    # Assert that the bot is listening for the next message
    client.listen.assert_called_with(12345)

    # Assert that the approval and hiding of join requests were called
    acc_client_mock.approve_all_chat_join_requests.assert_called_with(98765)
    acc_client_mock.hide_all_chat_join_requests.assert_called_with(98765)

    from unittest.mock import call
    # Assert that the edit calls were made in the correct order
    assert show_mock.edit.call_args_list == [
        call("**Now Forward A Message From Your Channel Or Group With Forward Tag\n\nMake Sure Your Logged In Account Is Admin In That Channel Or Group With Full Rights.**"),
        call("**Approving all join requests... Please wait until it's completed.**"),
        call("**Successfully approved all join requests.**")
    ]

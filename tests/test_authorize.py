from bookops_worldcat import __version__
from bookops_worldcat.authorize import AuthorizeAccess


def test_mocked_credentials(mock_credentials):
    assert mock_credentials == {
        "name": "TestCreds",
        "library": "OCLC",
        "key": "WSkey",
        "secret": "WSsecret",
        "authenticating_institution_id": "123456",
        "context_institution_id": "00001",
        "principal_id": "00000000-111a-222b-333c-4d444444444d",
        "principal_idns": "urn:oclc:platform:00001",
        "scope": ["scope1", "scope2"],
        "oauth_server": "https://oauth.oclc.test.org",
    }


class TestAuthorizeAccess:
    """Test AuthorizeAccess and obraining token"""

    def test_token_request_url():
        pass

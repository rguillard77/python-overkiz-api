from __future__ import annotations

from pyoverkiz.models import OverkizServer

COZYTOUCH_ATLANTIC_API = "https://api.groupe-atlantic.com"
COZYTOUCH_CLIENT_ID = (
    "czduc0RZZXdWbjVGbVV4UmlYN1pVSUM3ZFI4YTphSDEzOXZmbzA1ZGdqeDJkSFVSQkFTbmhCRW9h"
)

NEXITY_API = "https://api.egn.prd.aws-nexity.fr"
NEXITY_COGNITO_CLIENT_ID = "3mca95jd5ase5lfde65rerovok"
NEXITY_COGNITO_USER_POOL = "eu-west-1_wj277ucoI"
NEXITY_COGNITO_REGION = "eu-west-1"

SOMFY_API = "https://accounts.somfy.com"
SOMFY_CLIENT_ID = "0d8e920c-1478-11e7-a377-02dd59bd3041_1ewvaqmclfogo4kcsoo0c8k4kso884owg08sg8c40sk4go4ksg"
SOMFY_CLIENT_SECRET = "12k73w1n540g8o4cokg0cw84cog840k84cwggscwg884004kgk"

SUPPORTED_SERVERS: dict[str, OverkizServer] = {
    "atlantic_cozytouch": OverkizServer(
        name="Atlantic Cozytouch",
        endpoint="https://ha110-1.overkiz.com/enduser-mobile-web/enduserAPI/",
        manufacturer="Atlantic",
        configuration_url=None,
    ),
    "hi_kumo_asia": OverkizServer(
        name="Hitachi Hi Kumo (Asia)",
        endpoint="https://ha203-1.overkiz.com/enduser-mobile-web/enduserAPI/",
        manufacturer="Hitachi",
        configuration_url=None,
    ),
    "hi_kumo_europe": OverkizServer(
        name="Hitachi Hi Kumo (Europe)",
        endpoint="https://ha117-1.overkiz.com/enduser-mobile-web/enduserAPI/",
        manufacturer="Hitachi",
        configuration_url=None,
    ),
    "hi_kumo_oceania": OverkizServer(
        name="Hitachi Hi Kumo (Oceania)",
        endpoint="https://ha203-1.overkiz.com/enduser-mobile-web/enduserAPI/",
        manufacturer="Hitachi",
        configuration_url=None,
    ),
    "nexity": OverkizServer(
        name="Nexity Eugénie",
        endpoint="https://ha106-1.overkiz.com/enduser-mobile-web/enduserAPI/",
        manufacturer="Nexity",
        configuration_url=None,
    ),
    "rexel": OverkizServer(
        name="Rexel Energeasy Connect",
        endpoint="https://ha112-1.overkiz.com/enduser-mobile-web/enduserAPI/",
        manufacturer="Rexel",
        configuration_url="https://utilisateur.energeasyconnect.com/user/#/zone/equipements",
    ),
    "somfy_europe": OverkizServer(  # uses https://ha101-1.overkiz.com
        name="Somfy (Europe)",
        endpoint="https://tahomalink.com/enduser-mobile-web/enduserAPI/",
        manufacturer="Somfy",
        configuration_url="https://www.tahomalink.com",
    ),
    "somfy_america": OverkizServer(
        name="Somfy (North America)",
        endpoint="https://ha401-1.overkiz.com/enduser-mobile-web/enduserAPI/",
        manufacturer="Somfy",
        configuration_url=None,
    ),
    "somfy_oceania": OverkizServer(
        name="Somfy (Oceania)",
        endpoint="https://ha201-1.overkiz.com/enduser-mobile-web/enduserAPI/",
        manufacturer="Somfy",
        configuration_url=None,
    ),
}

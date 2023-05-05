import sgqlc.types
import sgqlc.types.datetime

fontawesome_schema = sgqlc.types.Schema()

########################################################################
# Scalars and Enumerations
########################################################################
Boolean = sgqlc.types.Boolean

Date = sgqlc.types.datetime.Date

ID = sgqlc.types.ID

Int = sgqlc.types.Int

String = sgqlc.types.String


########################################################################
# Input Objects
########################################################################
class SubsetIcon(sgqlc.types.Input):
    __schema__ = fontawesome_schema
    __field_names__ = ("name", "styles", "version")
    name = sgqlc.types.Field(String, graphql_name="name")
    styles = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name="styles")
    version = sgqlc.types.Field(String, graphql_name="version")


########################################################################
# Output Objects and Interfaces
########################################################################
class Account(sgqlc.types.Type):
    __schema__ = fontawesome_schema
    __field_names__ = ("email", "id", "kit", "kits", "pro_cdn_referrers")
    email = sgqlc.types.Field(String, graphql_name="email")
    id = sgqlc.types.Field(Int, graphql_name="id")
    kit = sgqlc.types.Field(
        "Kit",
        graphql_name="kit",
        args=sgqlc.types.ArgDict(
            (
                (
                    "token",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="token", default=None
                    ),
                ),
            )
        ),
    )
    kits = sgqlc.types.Field(sgqlc.types.list_of("Kit"), graphql_name="kits")
    pro_cdn_referrers = sgqlc.types.Field(
        "ProCdnReferrers", graphql_name="proCdnReferrers"
    )


class Download(sgqlc.types.Type):
    __schema__ = fontawesome_schema
    __field_names__ = ("separates_web_desktop",)
    separates_web_desktop = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="separatesWebDesktop"
    )


class FamilyStyle(sgqlc.types.Type):
    __schema__ = fontawesome_schema
    __field_names__ = ("family", "style")
    family = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="family")
    style = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="style")


class FamilyStylesByLicense(sgqlc.types.Type):
    __schema__ = fontawesome_schema
    __field_names__ = ("free", "pro")
    free = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FamilyStyle))),
        graphql_name="free",
    )
    pro = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FamilyStyle))),
        graphql_name="pro",
    )


class Icon(sgqlc.types.Type):
    __schema__ = fontawesome_schema
    __field_names__ = (
        "changes",
        "family_styles_by_license",
        "id",
        "label",
        "shim",
        "sris_by_license",
        "unicode",
    )
    changes = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
        graphql_name="changes",
    )
    family_styles_by_license = sgqlc.types.Field(
        sgqlc.types.non_null(FamilyStylesByLicense),
        graphql_name="familyStylesByLicense",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="id")
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="label")
    shim = sgqlc.types.Field("Shim", graphql_name="shim")
    sris_by_license = sgqlc.types.Field(
        sgqlc.types.non_null("SrisByLicense"), graphql_name="srisByLicense"
    )
    unicode = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="unicode")


class IconCount(sgqlc.types.Type):
    __schema__ = fontawesome_schema
    __field_names__ = ("free", "pro")
    free = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="free")
    pro = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="pro")


class IconUpload(sgqlc.types.Type):
    __schema__ = fontawesome_schema
    __field_names__ = ("height", "name", "path", "unicode", "version", "width")
    height = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="height")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")
    path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="path")
    unicode = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="unicode")
    version = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="version")
    width = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="width")


class Kit(sgqlc.types.Type):
    __schema__ = fontawesome_schema
    __field_names__ = (
        "auto_accessibility_enabled",
        "domains",
        "icon_uploads",
        "license_selected",
        "minified",
        "name",
        "release",
        "shim_enabled",
        "status",
        "technology_selected",
        "token",
        "version",
    )
    auto_accessibility_enabled = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="autoAccessibilityEnabled"
    )
    domains = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
        graphql_name="domains",
    )
    icon_uploads = sgqlc.types.Field(
        sgqlc.types.list_of(IconUpload), graphql_name="iconUploads"
    )
    license_selected = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="licenseSelected"
    )
    minified = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="minified")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")
    release = sgqlc.types.Field(sgqlc.types.non_null("Release"), graphql_name="release")
    shim_enabled = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="shimEnabled"
    )
    status = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="status")
    technology_selected = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="technologySelected"
    )
    token = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="token")
    version = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="version")


class Membership(sgqlc.types.Type):
    __schema__ = fontawesome_schema
    __field_names__ = ("free", "pro")
    free = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
        graphql_name="free",
    )
    pro = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
        graphql_name="pro",
    )


class ProCdnReferrers(sgqlc.types.Type):
    __schema__ = fontawesome_schema
    __field_names__ = ("active", "hostnames", "limit")
    active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="active")
    hostnames = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
        graphql_name="hostnames",
    )
    limit = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="limit")


class Release(sgqlc.types.Type):
    __schema__ = fontawesome_schema
    __field_names__ = (
        "date",
        "download",
        "icon_count",
        "icons",
        "is_latest",
        "sris_by_license",
        "version",
    )
    date = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name="date")
    download = sgqlc.types.Field(
        sgqlc.types.non_null(Download), graphql_name="download"
    )
    icon_count = sgqlc.types.Field(
        sgqlc.types.non_null(IconCount), graphql_name="iconCount"
    )
    icons = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Icon))),
        graphql_name="icons",
        args=sgqlc.types.ArgDict(
            (
                (
                    "license",
                    sgqlc.types.Arg(String, graphql_name="license", default=None),
                ),
            )
        ),
    )
    is_latest = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="isLatest"
    )
    sris_by_license = sgqlc.types.Field(
        sgqlc.types.non_null("SrisByLicense"), graphql_name="srisByLicense"
    )
    version = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="version")


class RootMutationType(sgqlc.types.Type):
    __schema__ = fontawesome_schema
    __field_names__ = ("create_subset",)
    create_subset = sgqlc.types.Field(
        "SubsetZipArchive",
        graphql_name="createSubset",
        args=sgqlc.types.ArgDict(
            (
                (
                    "icons",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(SubsetIcon),
                        graphql_name="icons",
                        default=None,
                    ),
                ),
                ("id", sgqlc.types.Arg(String, graphql_name="id", default=None)),
                (
                    "version",
                    sgqlc.types.Arg(String, graphql_name="version", default=None),
                ),
            )
        ),
    )


class RootQueryType(sgqlc.types.Type):
    __schema__ = fontawesome_schema
    __field_names__ = ("me", "release", "releases", "search")
    me = sgqlc.types.Field(Account, graphql_name="me")
    release = sgqlc.types.Field(
        Release,
        graphql_name="release",
        args=sgqlc.types.ArgDict(
            (
                (
                    "version",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="version",
                        default=None,
                    ),
                ),
            )
        ),
    )
    releases = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(Release)), graphql_name="releases"
    )
    search = sgqlc.types.Field(
        sgqlc.types.list_of(Icon),
        graphql_name="search",
        args=sgqlc.types.ArgDict(
            (
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=None)),
                (
                    "query",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="query", default=None
                    ),
                ),
                (
                    "version",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="version",
                        default=None,
                    ),
                ),
            )
        ),
    )


class RootSubscriptionType(sgqlc.types.Type):
    __schema__ = fontawesome_schema
    __field_names__ = ("subset_created",)
    subset_created = sgqlc.types.Field(
        "SubsetZipArchive",
        graphql_name="subsetCreated",
        args=sgqlc.types.ArgDict(
            (("id", sgqlc.types.Arg(String, graphql_name="id", default=None)),)
        ),
    )


class Shim(sgqlc.types.Type):
    __schema__ = fontawesome_schema
    __field_names__ = ("id", "name", "prefix")
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="id")
    name = sgqlc.types.Field(String, graphql_name="name")
    prefix = sgqlc.types.Field(String, graphql_name="prefix")


class Sri(sgqlc.types.Type):
    __schema__ = fontawesome_schema
    __field_names__ = ("path", "value")
    path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="path")
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class SrisByLicense(sgqlc.types.Type):
    __schema__ = fontawesome_schema
    __field_names__ = ("free", "pro")
    free = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Sri))),
        graphql_name="free",
    )
    pro = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Sri))),
        graphql_name="pro",
    )


class SubsetZipArchive(sgqlc.types.Type):
    __schema__ = fontawesome_schema
    __field_names__ = ("id", "ready_for_download", "url")
    id = sgqlc.types.Field(String, graphql_name="id")
    ready_for_download = sgqlc.types.Field(Boolean, graphql_name="readyForDownload")
    url = sgqlc.types.Field(String, graphql_name="url")


########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
fontawesome_schema.query_type = RootQueryType
fontawesome_schema.mutation_type = RootMutationType
fontawesome_schema.subscription_type = RootSubscriptionType

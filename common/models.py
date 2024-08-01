from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class COUNTRY(models.TextChoices):
    AF = "AF", "Afghanistan"
    AL = "AL", "Albania"
    DZ = "DZ", "Algeria"
    AS = "AS", "American Samoa"
    AD = "AD", "Andorra"
    AO = "AO", "Angola"
    AI = "AI", "Anguilla"
    AQ = "AQ", "Antarctica"
    AG = "AG", "Antigua and Barbuda"
    AR = "AR", "Argentina"
    AM = "AM", "Armenia"
    AW = "AW", "Aruba"
    AU = "AU", "Australia"
    AT = "AT", "Austria"
    AZ = "AZ", "Azerbaijan"
    BS = "BS", "Bahamas"
    BH = "BH", "Bahrain"
    BD = "BD", "Bangladesh"
    BB = "BB", "Barbados"
    BY = "BY", "Belarus"
    BE = "BE", "Belgium"
    BZ = "BZ", "Belize"
    BJ = "BJ", "Benin"
    BM = "BM", "Bermuda"
    BT = "BT", "Bhutan"
    BO = "BO", "Bolivia"
    BA = "BA", "Bosnia and Herzegovina"
    BW = "BW", "Botswana"
    BR = "BR", "Brazil"
    IO = "IO", "British Indian Ocean Territory"
    VG = "VG", "British Virgin Islands"
    BN = "BN", "Brunei"
    BG = "BG", "Bulgaria"
    BF = "BF", "Burkina Faso"
    BI = "BI", "Burundi"
    CV = "CV", "Cabo Verde"
    KH = "KH", "Cambodia"
    CM = "CM", "Cameroon"
    CA = "CA", "Canada"
    KY = "KY", "Cayman Islands"
    CF = "CF", "Central African Republic"
    TD = "TD", "Chad"
    CL = "CL", "Chile"
    CN = "CN", "China"
    CO = "CO", "Colombia"
    KM = "KM", "Comoros"
    CD = "CD", "Congo - Kinshasa"
    CG = "CG", "Congo - Brazzaville"
    CK = "CK", "Cook Islands"
    CR = "CR", "Costa Rica"
    CI = "CI", "Côte d’Ivoire"
    HR = "HR", "Croatia"
    CU = "CU", "Cuba"
    CY = "CY", "Cyprus"
    CZ = "CZ", "Czechia"
    DK = "DK", "Denmark"
    DJ = "DJ", "Djibouti"
    DM = "DM", "Dominica"
    DO = "DO", "Dominican Republic"
    EC = "EC", "Ecuador"
    EG = "EG", "Egypt"
    SV = "SV", "El Salvador"
    GQ = "GQ", "Equatorial Guinea"
    ER = "ER", "Eritrea"
    EE = "EE", "Estonia"
    SZ = "SZ", "Eswatini"
    ET = "ET", "Ethiopia"
    FJ = "FJ", "Fiji"
    FI = "FI", "Finland"
    FR = "FR", "France"
    GF = "GF", "French Guiana"
    PF = "PF", "French Polynesia"
    GA = "GA", "Gabon"
    GM = "GM", "Gambia"
    GE = "GE", "Georgia"
    DE = "DE", "Germany"
    GH = "GH", "Ghana"
    GI = "GI", "Gibraltar"
    GR = "GR", "Greece"
    GL = "GL", "Greenland"
    GD = "GD", "Grenada"
    GP = "GP", "Guadeloupe"
    GU = "GU", "Guam"
    GT = "GT", "Guatemala"
    GG = "GG", "Guernsey"
    GN = "GN", "Guinea"
    GW = "GW", "Guinea-Bissau"
    GY = "GY", "Guyana"
    HT = "HT", "Haiti"
    HN = "HN", "Honduras"
    HK = "HK", "Hong Kong SAR China"
    HU = "HU", "Hungary"
    IS = "IS", "Iceland"
    IN = "IN", "India"
    ID = "ID", "Indonesia"
    IR = "IR", "Iran"
    IQ = "IQ", "Iraq"
    IE = "IE", "Ireland"
    IM = "IM", "Isle of Man"
    IL = "IL", "Israel"
    IT = "IT", "Italy"
    JM = "JM", "Jamaica"
    JP = "JP", "Japan"
    JE = "JE", "Jersey"
    JO = "JO", "Jordan"
    KZ = "KZ", "Kazakhstan"
    KE = "KE", "Kenya"
    KI = "KI", "Kiribati"
    XK = "XK", "Kosovo"
    KW = "KW", "Kuwait"
    KG = "KG", "Kyrgyzstan"
    LA = "LA", "Laos"
    LV = "LV", "Latvia"
    LB = "LB", "Lebanon"
    LS = "LS", "Lesotho"
    LR = "LR", "Liberia"
    LY = "LY", "Libya"
    LI = "LI", "Liechtenstein"
    LT = "LT", "Lithuania"
    LU = "LU", "Luxembourg"
    MO = "MO", "Macau SAR China"
    MG = "MG", "Madagascar"
    MW = "MW", "Malawi"
    MY = "MY", "Malaysia"
    MV = "MV", "Maldives"
    ML = "ML", "Mali"
    MT = "MT", "Malta"
    MH = "MH", "Marshall Islands"
    MQ = "MQ", "Martinique"
    MR = "MR", "Mauritania"
    MU = "MU", "Mauritius"
    YT = "YT", "Mayotte"
    MX = "MX", "Mexico"
    FM = "FM", "Micronesia"
    MD = "MD", "Moldova"
    MC = "MC", "Monaco"
    MN = "MN", "Mongolia"
    ME = "ME", "Montenegro"
    MS = "MS", "Montserrat"
    MA = "MA", "Morocco"
    MZ = "MZ", "Mozambique"
    MM = "MM", "Myanmar (Burma)"
    NA = "NA", "Namibia"
    NR = "NR", "Nauru"
    NP = "NP", "Nepal"
    NL = "NL", "Netherlands"
    NC = "NC", "New Caledonia"
    NZ = "NZ", "New Zealand"
    NI = "NI", "Nicaragua"
    NE = "NE", "Niger"
    NG = "NG", "Nigeria"
    NU = "NU", "Niue"
    NF = "NF", "Norfolk Island"
    KP = "KP", "North Korea"
    MK = "MK", "North Macedonia"
    MP = "MP", "Northern Mariana Islands"
    NO = "NO", "Norway"
    OM = "OM", "Oman"
    PK = "PK", "Pakistan"
    PW = "PW", "Palau"
    PS = "PS", "Palestinian Territories"
    PA = "PA", "Panama"
    PG = "PG", "Papua New Guinea"
    PY = "PY", "Paraguay"
    PE = "PE", "Peru"
    PH = "PH", "Philippines"
    PN = "PN", "Pitcairn Islands"
    PL = "PL", "Poland"
    PT = "PT", "Portugal"
    PR = "PR", "Puerto Rico"
    QA = "QA", "Qatar"
    RE = "RE", "Réunion"
    RO = "RO", "Romania"
    RU = "RU", "Russia"
    RW = "RW", "Rwanda"
    WS = "WS", "Samoa"
    SM = "SM", "San Marino"
    ST = "ST", "São Tomé and Príncipe"
    SA = "SA", "Saudi Arabia"
    SN = "SN", "Senegal"
    RS = "RS", "Serbia"
    SC = "SC", "Seychelles"
    SL = "SL", "Sierra Leone"
    SG = "SG", "Singapore"
    SX = "SX", "Sint Maarten"
    SK = "SK", "Slovakia"
    SI = "SI", "Slovenia"
    SB = "SB", "Solomon Islands"
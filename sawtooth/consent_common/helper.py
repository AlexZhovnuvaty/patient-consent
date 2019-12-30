import hashlib

DISTRIBUTION_NAME = 'patient-consent'

DEFAULT_URL = 'http://127.0.0.1:8009'

TP_FAMILYNAME = 'consent'
TP_VERSION = '1.0'
<<<<<<< HEAD
PERMISSION_ENTITY_CODE = '01'
CLIENT_ENTITY_CODE = '02'
PERMISSION_TYPE = '03'

INFORM_DOCUMENT_CONSENT = '01'
DATA_PROCESSING_ACCESS = '02'
INVESTIGATOR_ACCESS = '03'  # Consent by Patient to Hospital
INFORM_DOCUMENT_REQUEST = '04'  # Consent by Hospital to Data Provider
=======
CONSENT_ENTITY_CODE = '01'
CLIENT_ENTITY_CODE = '02'
CONSENT_TYPE = '03'

CONSENT_READ_EHR = '01'
CONSENT_WRITE_EHR = '02'
CONSENT_SHARE_EHR = '03'  # Consent by Patient to Hospital
CONSENT_SHARE_SHARED_EHR = '04'  # Consent by Hospital to Data Provider
>>>>>>> upstream/master


def _hash(identifier):
    return hashlib.sha512(identifier.encode('utf-8')).hexdigest()


TP_PREFFIX_HEX6 = _hash(TP_FAMILYNAME)[0:6]


def make_client_address(public_key):
    return TP_PREFFIX_HEX6 + CLIENT_ENTITY_CODE + _hash(public_key)[:62]


<<<<<<< HEAD
def make_investigator_access_address(dest_pkey, src_pkey):
    return make_permission_address(INVESTIGATOR_ACCESS, dest_pkey, src_pkey)


def make_sign_inform_document_consent_address(dest_pkey, src_pkey):
    return make_permission_address(INFORM_DOCUMENT_CONSENT, dest_pkey, src_pkey)


def make_data_processing_access_address(dest_pkey, src_pkey):
    return make_permission_address(DATA_PROCESSING_ACCESS, dest_pkey, src_pkey)


def make_request_inform_document_consent_address(dest_pkey, src_pkey):
    return make_permission_address(INFORM_DOCUMENT_REQUEST, dest_pkey, src_pkey)


def make_permission_address(permission_type, dest_pkey, src_pkey):
    return TP_PREFFIX_HEX6 + PERMISSION_ENTITY_CODE \
           + PERMISSION_TYPE + _hash(permission_type)[:4] \
=======
def make_consent_read_ehr_address(dest_pkey, src_pkey):
    return make_consent_address(CONSENT_READ_EHR, dest_pkey, src_pkey)


def make_consent_write_ehr_address(dest_pkey, src_pkey):
    return make_consent_address(CONSENT_WRITE_EHR, dest_pkey, src_pkey)


def make_consent_share_ehr_address(dest_pkey, src_pkey):
    return make_consent_address(CONSENT_SHARE_EHR, dest_pkey, src_pkey)


def make_consent_share_shared_ehr_address(dest_pkey, src_pkey):
    return make_consent_address(CONSENT_SHARE_SHARED_EHR, dest_pkey, src_pkey)


def make_consent_address(consent_type, dest_pkey, src_pkey):
    return TP_PREFFIX_HEX6 + CONSENT_ENTITY_CODE \
           + CONSENT_TYPE + _hash(consent_type)[:4] \
>>>>>>> upstream/master
           + CLIENT_ENTITY_CODE + _hash(dest_pkey)[:26] \
           + CLIENT_ENTITY_CODE + _hash(src_pkey)[:26]


<<<<<<< HEAD
def make_permission_list_address():
    return TP_PREFFIX_HEX6 + PERMISSION_ENTITY_CODE


def make_permission_list_address_by_destination_client(permission_type, dest_pkey):
    return TP_PREFFIX_HEX6 + PERMISSION_ENTITY_CODE \
           + PERMISSION_TYPE + _hash(permission_type)[:4] \
           + CLIENT_ENTITY_CODE + _hash(dest_pkey)[:26]


def make_investigator_access_list_address_by_destination_client(dest_pkey):
    return make_permission_list_address_by_destination_client(INVESTIGATOR_ACCESS, dest_pkey)


def make_sign_inform_document_consent_list_address_by_destination_client(dest_pkey):
    return make_permission_list_address_by_destination_client(INFORM_DOCUMENT_CONSENT, dest_pkey)


def make_data_processing_access_list_address_by_destination_client(dest_pkey):
    return make_permission_list_address_by_destination_client(DATA_PROCESSING_ACCESS, dest_pkey)


def make_request_inform_document_consent_list_address_by_destination_client(dest_pkey):
    return make_permission_list_address_by_destination_client(INFORM_DOCUMENT_REQUEST, dest_pkey)
=======
def make_consent_list_address():
    return TP_PREFFIX_HEX6 + CONSENT_ENTITY_CODE


def make_consent_list_address_by_destination_client(consent_type, dest_pkey):
    return TP_PREFFIX_HEX6 + CONSENT_ENTITY_CODE \
           + CONSENT_TYPE + _hash(consent_type)[:4] \
           + CLIENT_ENTITY_CODE + _hash(dest_pkey)[:26]


def make_consent_read_ehr_list_address_by_destination_client(dest_pkey):
    return make_consent_list_address_by_destination_client(CONSENT_READ_EHR, dest_pkey)


def make_consent_write_ehr_list_address_by_destination_client(dest_pkey):
    return make_consent_list_address_by_destination_client(CONSENT_WRITE_EHR, dest_pkey)


def make_consent_share_ehr_list_address_by_destination_client(dest_pkey):
    return make_consent_list_address_by_destination_client(CONSENT_SHARE_EHR, dest_pkey)


def make_consent_share_shared_ehr_list_address_by_destination_client(dest_pkey):
    return make_consent_list_address_by_destination_client(CONSENT_SHARE_SHARED_EHR, dest_pkey)
>>>>>>> upstream/master

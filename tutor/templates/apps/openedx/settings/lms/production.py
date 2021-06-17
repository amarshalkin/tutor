# -*- coding: utf-8 -*-
import os
from lms.envs.production import *

{% include "apps/openedx/settings/partials/common_lms.py" %}

ALLOWED_HOSTS = [
    ENV_TOKENS.get("LMS_BASE"),
    FEATURES["PREVIEW_LMS_BASE"],
    "lms",
]

{% if ENABLE_HTTPS %}
# Properly set the "secure" attribute on session/csrf cookies. This is required in
# Chrome to support samesite=none cookies.
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
DCS_SESSION_COOKIE_SAMESITE = "None"
{% else %}
# When we cannot provide secure session/csrf cookies, we must disable samesite=none
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
DCS_SESSION_COOKIE_SAMESITE = "Lax"
{% endif %}

# Required to display all courses on start page
SEARCH_SKIP_ENROLLMENT_START_DATE_FILTERING = True

# Enable edx-enterprise features
LMS_ROOT_URL = ENV_TOKENS.get("LMS_ROOT_URL")

SYSTEM_WIDE_ROLE_CLASSES.append('enterprise.SystemWideEnterpriseUserRoleAssignment')
ENTERPRISE_API_URL = f"{ LMS_ROOT_URL }/enterprise/api/v1/"

ENTERPRISE_LEARNER_PORTAL_NETLOC = 'learner.lms.knotta.ru'
ENTERPRISE_LEARNER_PORTAL_BASE_URL = 'https://' + ENTERPRISE_LEARNER_PORTAL_NETLOC

ENTERPRISE_ADMIN_PORTAL_NETLOC = 'enterprise.lms.knotta.ru'
ENTERPRISE_ADMIN_PORTAL_BASE_URL = 'https://' + ENTERPRISE_ADMIN_PORTAL_NETLOC

ENTERPRISE_CATALOG_INTERNAL_ROOT_URL = 'http://enterprise.catalog.app:18160'

# LOGIN_REDIRECT_WHITELIST.append(ENTERPRISE_LEARNER_PORTAL_NETLOC)
# LOGIN_REDIRECT_WHITELIST.append(ENTERPRISE_ADMIN_PORTAL_NETLOC)

FEATURES.update({"ENABLE_ENTERPRISE_INTEGRATION": True})

MKTG_URLS.update({'ENTERPRISE': '/enterprise'})

{{ patch("openedx-lms-production-settings") }}

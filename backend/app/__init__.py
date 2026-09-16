

# Infriqa Managed Deploy QA — intentional CORS change for Cloud Impact
# Safe to revert after testing Deploy Live App alert.
CORS_ORIGINS = ["*"]  # wildcard — triggers cors_policy detector
allowed_origins = CORS_ORIGINS

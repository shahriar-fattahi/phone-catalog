from django.contrib.auth.mixins import AccessMixin


class AdminRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            if not request.user.is_admin:
                return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

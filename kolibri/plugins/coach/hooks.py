from __future__ import absolute_import, print_function, unicode_literals
from kolibri.core.webpack import hooks as webpack_hooks


class CoachSyncHook(webpack_hooks.WebpackInclusionHook):
    """
    Inherit a hook defining assets to be loaded synchronously in coach/coach.html
    """

    class Meta:
        abstract = True


class CoachAsyncHook(webpack_hooks.WebpackInclusionHook):
    """
    Inherit a hook defining assets to be loaded asynchronously in coach/coach.html
    """

    class Meta:
        abstract = True

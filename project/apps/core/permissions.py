from rest_framework import permissions

class IsUserOrReadOnly(permissions.BasePermission):
	"""
	Allows a user to view and edit his own user object, but only view another user's
	"""

	def has_object_permission(self, request, view, obj):
		# Read permissions are allowed for any request
		if request.method in permissions.SAFE_METHODS:
			return True

		#request.user must be the same as obj
		return obj == request.user
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserDisplaySerializer


class CurrentUserAPIView(APIView):
    """
    View to return the username of the current user
    logged in the system.

    * Requires token authentication.
    * Only authenticated users are able to access this view.
    """
    def get(self, request):
        '''
        Return the username of the current user.
        '''
        serializer = UserDisplaySerializer(request.user)
        return Response(serializer.data)

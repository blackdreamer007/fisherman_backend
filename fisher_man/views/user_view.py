from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from fisher_man.models.user import User
from fisher_man.serializers.user_serializer import UserSerializer, UserEditSerializer
from django.contrib.auth.hashers import check_password, make_password

# Signup View
class SignupView(APIView):
    def post(self, request):
        mobile = request.data.get("mobile")

        if User.objects.filter(mobile=mobile).exists():
            return Response(
                {"error": "Mobile already registered"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User created successfully"},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Signin View
class SigninView(APIView):
    def post(self, request):
        mobile = request.data.get('mobile')
        password = request.data.get('password')

        if not mobile or not password:
            return Response(
                {"error": "Mobile and password are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = User.objects.get(mobile=mobile)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        if not check_password(password, user.password):
            return Response(
                {"error": "Invalid password"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        if user.is_active is False:
            return Response(
                {"error": "User is inactive"},
                status=status.HTTP_403_FORBIDDEN
            )

        # Session
        request.session["user_id"] = user.id

        #return Response({"message": "Signin successful",}, status=status.HTTP_200_OK)
        return Response({
            "message": "Signin successful",
            "user_id": user.id,
            "user_type": user.user_type,
        }, status=status.HTTP_200_OK)


class ChangePasswordView(APIView):
    def post(self, request):
        mobile = request.data.get("mobile")
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")

        if not mobile or not old_password or not new_password:
            return Response(
                {"error": "Mobile, old password and new password are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = User.objects.get(mobile=mobile)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        # Check old password
        if not check_password(old_password, user.password):
            return Response(
                {"error": "Old password is incorrect"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        # Set new password
        user.password = make_password(new_password)
        user.save()

        return Response(
            {"message": "Password changed successfully"},
            status=status.HTTP_200_OK
        )


class EditProfileView(APIView):
    def put(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = UserEditSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Profile updated successfully"},
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
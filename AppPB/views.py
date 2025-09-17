from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Portfolio, GalleryImage
from .serializers import PortfolioSerializer
from rest_framework import generics
from .models import ContactMessage
from .serializers import ContactMessageSerializer
import re


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        # Save the main Portfolio object
        portfolio = serializer.save()

        # Save the gallery images separately
        gallery_files = self.request.FILES.getlist('gallery_images')
        for image in gallery_files:
            GalleryImage.objects.create(portfolio=portfolio, image=image)


@api_view(["POST"])
def signup(request):
    try:
        name = request.data.get("name")
        email = request.data.get("email")
        password = request.data.get("password")

        if not name or not email or not password:
            return Response({"error": "All fields are required"}, status=400)

        if User.objects.filter(username=email).exists():
            return Response({"error": "Email already registered"}, status=400)

        # password validation
        if len(password) < 8:
            return Response({"error": "Password must be at least 8 characters"}, status=400)
        if not re.search(r"[A-Z]", password):
            return Response({"error": "Password must contain an uppercase letter"}, status=400)
        if not re.search(r"[a-z]", password):
            return Response({"error": "Password must contain a lowercase letter"}, status=400)
        if not re.search(r"[0-9]", password):
            return Response({"error": "Password must contain a number"}, status=400)
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return Response({"error": "Password must contain a special character"}, status=400)

        # ✅ Create user
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=name
        )

        # ✅ Generate JWT token
        refresh = RefreshToken.for_user(user)
        return Response({
            "message": "User created successfully",
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }, status=201)

    except Exception as e:
        return Response({"error": str(e)}, status=500)





@api_view(["POST"])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")
    user = authenticate(username=email, password=password)

    if user is None:
        return Response({"error": "Invalid credentials"}, status=400)

    refresh = RefreshToken.for_user(user)
    return Response({
        "refresh": str(refresh),
        "access": str(refresh.access_token),
        "user": {"id": user.id, "name": user.first_name, "email": user.email}
    })


class ContactMessageCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

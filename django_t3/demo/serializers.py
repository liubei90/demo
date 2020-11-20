from django.db.models.base import Model
from .models import DOptions, DPosts, DUsers, DUsermeta
from rest_framework import serializers, viewsets, routers


class DPostsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DPosts
        fields = ['blog_id', 'site_id', 'domain', 'path', 'public']


class DPostsViewSet(viewsets.ModelViewSet):
    queryset = DPosts.objects.all()
    serializer_class = DPostsSerializer


class DOptionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DOptions
        fields = ['option_id', 'option_name', 'option_value', 'autoload']


class DOptionsViewSet(viewsets.ModelViewSet):
    queryset = DOptions.objects.all()
    serializer_class = DOptionsSerializer


class DUsermetaSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(queryset=DUsers.objects.all())

    class Meta:
        model = DUsermeta
        fields = ['umeta_id', 'user_id', 'meta_key', 'meta_value']


class DUsermetaViewSet(viewsets.ModelViewSet):
    queryset = DUsermeta.objects.all()
    serializer_class = DUsermetaSerializer


class DUsersSerializer(serializers.ModelSerializer):
    # usersmetas = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # usersmetas = serializers.PrimaryKeyRelatedField(many=True, allow_null=True, queryset=DUsermeta.objects.all())
    usersmetas = DUsermetaSerializer(many=True, read_only=True)

    class Meta:
        model = DUsers
        fields = ['id', 'user_login', 'user_pass', 'user_nicename', 'user_email', 'user_url', 'user_registered', 'user_activation_key', 'user_status', 'display_name', 'usersmetas']

    # def create(self, validated_data):
    #     usermetas = validated_data.pop('usermetas')
    #     user = DUsers.objects.create(**validated_data)
    #     # DUsermeta.objects.create(user=user, **usermetas)
    #     # user['usermetas'] = usermetas
    #     return user


class DUsersViewSet(viewsets.ModelViewSet):
    queryset = DUsers.objects.all()
    serializer_class = DUsersSerializer


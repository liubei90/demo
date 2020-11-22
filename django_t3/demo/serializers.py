from django.db.models.base import Model
from rest_framework import serializers, viewsets, routers
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import DOptions, DPosts, DUsers, DUsermeta

class DPostsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DPosts
        fields = ['id', 'post_author', 'post_date', 'post_title', 'post_content', 
            'post_status', 'comment_status', 'post_parent', 'comment_count']


class DPostsViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = DPosts.objects.all()
    serializer_class = DPostsSerializer

    def get_permissions(self):
        print(self.action)
        permission_actions = ['create', 'update', 'partial_update', 'destroy']

        # 部分方法需要权限
        if self.action in permission_actions:
            return [IsAuthenticated()]

        return []


class DOptionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DOptions
        fields = ['option_id', 'option_name', 'option_value', 'autoload']


class DOptionsViewSet(viewsets.ModelViewSet):
    queryset = DOptions.objects.all()
    serializer_class = DOptionsSerializer


# class DUsermetaListSerializer(serializers.ListSerializer):
#     def update(self, instance, validated_data):
#         print(type(instance))
#         print(validated_data)
#         return instance


class DUsermetaSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(queryset=DUsers.objects.all())

    class Meta:
        model = DUsermeta
        fields = ['umeta_id', 'user_id', 'meta_key', 'meta_value']
        # list_serializer_class = DUsermetaListSerializer

    # def update(self, instance, validated_data):
    #     print(instance)
    #     print(validated_data)


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
    #     usermetas = validated_data.pop('usersmetas')
    #     user = DUsers.objects.create(**validated_data)

    #     for meta in usermetas:
    #         DUsermeta.objects.create(user=user, **meta)

    #     return user

    # def update(self, instance, validated_data):
    #     # 更新users ，忽略传入的 usersmetas 字段
    #     update_fields = [k for k in list(self.fields.keys()) if k not in ['usersmetas']]

    #     for k in update_fields:
    #         setattr(instance, k, validated_data.get(k, getattr(instance, k)))

    #     instance.save()

    #     # 一对多的更新，不应该放在该处做，应该多的列表中有个批量修改接口
    #     # 更新关联的usermetas
    #     # newmetas = validated_data.get('usersmetas')

    #     # if newmetas:
    #     #     oldmetas = instance.usersmetas.all()
    #     #     oldmetas_map = {m.umeta_id: m for m in oldmetas}
    #     #     newmetas_map = { m['umeta_id']: m for m in newmetas }

    #     #     # 更新已有的数据

    #     return instance


class DUsersViewSet(viewsets.ModelViewSet):
    queryset = DUsers.objects.all()
    serializer_class = DUsersSerializer


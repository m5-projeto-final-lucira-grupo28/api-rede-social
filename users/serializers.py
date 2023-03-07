from rest_framework import serializers
from .models import User

# def choices_error_message(choices_class):
#     valid_choices = [choice[0] for choice in choices_class]
#     message = ", ".join(valid_choices).rsplit(",", 1)

#     return "Choose between " + " and".join(message) + "."


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "password",
            "first_name",
            "last_name",
            "birthdate",
            "gender",
            "followers_friendships"
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "followers_friendships": {"read_only": True}
        }

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)
            if key == "password":
                instance.set_password(value)
        instance.save()

        return instance
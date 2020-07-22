from rest_framework import serializers

from .models import Categories, Theme, Words, Levels


class CaregoriesSerializer(serializers.ModelSerializer):
    """Categories serializer"""
    class Meta:
        model = Categories
        fields = ("id", "name", "icon")


class LevelsSerializer(serializers.ModelSerializer):
    """Levels serializer"""
    class Meta:
        model = Levels
        fields = ("id", "name", "code")


class WordsSerializer(serializers.ModelSerializer):
    """Words serializer"""
    class Meta:
        model = Words
        fields = ("id", "name", "translation", "transcription", "example", "sound")


class ThemesSerializer(serializers.ModelSerializer):
    """Themes serializer"""
    class Meta:
        model = Theme
        exclude = ()




class ThemeSerializer(serializers.ModelSerializer):
    """Theme serializer"""
    words_to_theme = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    class Meta:
        model = Theme
        exclude = ()
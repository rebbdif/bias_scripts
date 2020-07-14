from enum import Enum


class MessageType(Enum):
    GENERIC = "Message",
    TEXT = "TextMessage",
    STICKER = "StickerMessage",
    PHOTO = "PhotoMessage",
    VIDEO = "VideoMessage",
    VIDEO_NOTE = "VideoNoteMessage",
    #
    AUDIO = "AudioMessage",
    VOICE = "VoiceMessage",
    DOCUMENT = "DocumentMessage",
    ANIMATION = "AnimationMessage",

    def raw_value(self):
        return self.value[0]

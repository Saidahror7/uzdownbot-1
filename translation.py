class Translation(object):
    START_TEXT = """<b>🙋Assalom Alaykum Men URL Orqali Fayllarni Yuklab Beruvchi Bot Bo'laman</b>

Menga url Yuboring

Barcha Malumotlar /help Bo'limida..

Aloqa : @JokkerKing"""
    RENAME_403_ERR = "Uzur. Faylni Qayta Nomlash Bajarilmadi."
    ABS_TEXT = " Please don't be selfish."
    UPGRADE_TEXT = "<b>😅Bu Tekin Sevis. Yangilash Uchun  Plan Mavjud emas 😜</b>  Malumot Uchun /help"
    FORMAT_SELECTION = "Fayl formatini Tanlang: <a href='{}'>fayl hajmi taxminiy bo'lishi mumkin</a>
Agar siz o'zingizning shaxsiy eskizingizni o'rnatmoqchi bo'lsangiz, quyidagi tugmalarni bosganingizdan oldin yoki tezda suratni yuboring.
Avtomatik yaratilgan eskizni o'chirish uchun siz /deletethumbnail tugmachasidan foydalanishingiz mumkin.
Agar siz premium videolarni yuklab olishni xohlasangiz, quyidagi formatda taqdim eting:
URL | fayl nomi | foydalanuvchi nomi | parol"
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | filename | username | password"""
    NOYES_URL = "@robot URL detected. Please use https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    DOWNLOAD_START = "<b>Yublab olinmoqda📥 </b>"
    UPLOAD_START = "<b>Jo'natilmoqga📥</b>"
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    RCHD_TG_API_LIMIT = "Yuklashga Ketgan vaqt: {} sekund.\nFayl Hajmi: {}\nUzur. Ammo, men Telegram API cheklovlari tufayli 1.5 Gb dan katta fayllarni yuklay olmayman"
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Iltimos, meni foydali deb bilsangiz, baholang. https://t.me/tlgrmcbot?start=allonetgbot-review Admin : @JokkerKing"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "📥Yuklashga Ketgan vaqt: {} sekund. \n📣Kanalga a'zo Boling : @Online_Tutorial \n📤Jo'natishga Ketgan vaqt: {} seund."
    NOT_AUTH_USER_TEXT = "Please /upgrade your subscription."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload: {}\nPlease /upgrade your subscription.\nIf you think this is a bug, please contact <a href='https://telegram.me/jokkerking>@Support : @JokkerKing</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Shaxsiy video / fayl eskizi saqlandi. Ushbu rasm video / faylda ishlatiladi. "
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Foydalanuvchi rasmlari muvaffaqiyatli o'chirildi."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "Foydalanuvchi rasmlari topilmadi."
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    CURENT_PLAN_DETAILS = """Current plan details
FULL FREE😅
Telegram ID: <code>{}</code>
Plan name: Free  User
Expires on: 31/12/2020
Contact: @JokkerKing"""
    HELP_USER = """Salom, URL yuklash uchun.
    
1. URL manzilini yuboring (url|kengaytmali yangi nom).
2. Shaxsiy eskizni yuboring (ixtiyoriy).
3. Tugmani tanlang.
   SVideo - Skrinshotlar yordamida faylni video sifatida berish
   DFile - Skrinshot bilan fayl berish
   Video - Faylni skrinshotisiz video sifatida berish
   DFile - Faylni ekran tasvirisiz berish

/getlink - yuqori tezlikda  yuklab olish havolasini olish.

/converttoaudio - Telegram-dagi videofayllarni audio-fayllarga aylantirish


/converttovideo - faylni videoga aylantirish.

/rename-  Qayta Nomlash.
/extractstreams - Telegram Media-dan oqimlarni ajratib oling

/ffmpegrobot - ma\'lumot oling
bezak va TimeStamp-ni kiriting.

/downloadmedia - Mediani saqlash uchun yuklab oling.

/storageinfo - Hozirda saqlangan media haqida ma'lumot oling

/unzip - Telegramdan turib zip fayllarni chiqarib oling.

/generatecustomthumbnail - Odatiy videolar uchun eskiz yaratish.

/generatescss - Telegram Media-ning skrinshotini yarating.

Joriy reja tafsilotlarini bilish uchun menga /me yuboring

Qo\'llab-quvvatlash: @JokkerKing"""
    REPLY_TO_DOC_GET_LINK = "Yuqori tezlikda to\'g\'ridan-to\'g\'ri yuklab olish havolasini olish uchun Telegram media-ga javob bering"
    REPLY_TO_DOC_FOR_C2V = "O\'zgartirish uchun Telegram media-ga javob bering"
    REPLY_TO_DOC_FOR_SCSS = "Reply to a Telegram media to get screenshots"
    REPLY_TO_DOC_FOR_RENAME_FILE = "Reply to a Telegram media to /rename with custom thumbnail support"
    AFTER_GET_DL_LINK = "Direct Link <a href='{}'>Yaratildi</a> Muddati {} Kun.\n© @Jokkerking"
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Syntax: /trim HH:MM:SS [HH:MM:SS]"""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "Avval biron bir faylni mening hotiramga yuklab olish uchun /downloadmedia \nHozir yuklab olingan media fayllarni bilish uchun ma\'lumot /storageinfo yuboring."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video davomiyligi: {} \ nUshbu mediani saqlash joyimdan o\'chirish uchun /clearffmpegmedia yuboring
Qirqish uchun /trim HH:MMSS."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "Saqlangan media allaqachon mavjud. Mavjud media tafsilotlarini bilish uchun iltimos, /storageinfo yuboring"
    USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> deleted from DataBase."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "Reply to a Telegram media (MKV), to extract embedded streams"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Shaxsiy rasmlarni yaratish uchun media albomga javob bering / generatecustomthumbnail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Albomda faqat ikkita fotosurat bo'lishi kerak. Iltimos, media albomni qayta yuboring va yana urinib ko'ring yoki albomga faqat ikkita rasmni yuboring."
    INVALID_UPLOAD_BOT_URL_FORMAT = "URL formati noto\‘g\‘ri. URL manzilingiz http: // yoki https: // bilan boshlanganiga ishonch hosil qiling. Format havolasi | yordamida, siz maxsus fayl nomini qo'yishingiz mumkin file_name.extension"
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "https://telegram.dog/FFMpegRoBot"
    EXTRACT_ZIP_INTRO_ONE = "Avval zip faylni yuboring, so\'ngra faylga javob /unzip buyrug'ini yuboring."
    EXTRACT_ZIP_INTRO_THREE = "Qabul qilingan faylni tahlil qilish. ⚠️ Bu biroz vaqt talab qilishi mumkin. Iltimos, sabr qiling."
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Kechirasiz. zip faylni qayta ishlash paytida xatolar yuz berdi. Iltimos, hamma narsani yana ikki marta tekshiring va agar muammo takrorlansa, bu haqda xabar bering <a href='https://telegram.me/jokkerking>@JokkerKing</a>"
    EXTRACT_ZIP_STEP_TWO = """Quyidagi variantlardan yuklash uchun file_name tanlang.
Faylni olganingizdan so\'ng, uni kichik rasmlarni qo\'llab-quvvatlash bilan /rename buyruqdan foydalanishingiz mumkin."""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    FREE_USER_LIMIT_Q_SZE = """Cannot Process.
Free users only 1 request per 30 minutes.
/upgrade or Try 1800 seconds later."""
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."

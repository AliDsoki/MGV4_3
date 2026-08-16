# -*- coding: utf-8 -*-
"""
MGV4_3.py - نسخة ملف واحد من برنامج MG Downloader (PyQt6).

التغييرات الأساسية في هذه النسخة (4.3):
- إصدار البرنامج: 4.3.
- [إصلاح 4.3] السبب الجذري لتعطّل البرنامج المفاجئ عند فتح/استخدام
  "قائمة الانتظار": بطاقة الرابط كانت في حالات معيّنة تبدأ ثريد تحميل
  الصورة المصغّرة مرتين متتاليتين (مرة عند إنشاء البطاقة ومرة أخرى فوراً
  من داخل التحديث الأول لها)، فيفقد الثريد الأول (الذي لا يزال يعمل
  فعلياً) آخر مرجع له ويُدمَّر فجأة أثناء عمله — وهو ما يظهر في الطرفية
  كرسالة "QThread: Destroyed while thread is still running" ويُغلق
  البرنامج بالكامل. الآن لا تبدأ البطاقة ثريداً جديداً طالما هناك ثريد
  سابق لنفس الصورة لا يزال يعمل.
- [جديد 4.3] نافذة قائمة الانتظار أصبحت تُنشأ مرة واحدة فقط وتبقى حيّة
  طوال عمل البرنامج (تُخفى بدل أن تُغلق/تُدمَّر)، وأي ثريد تحميل صورة لا
  يزال يعمل يُنتظر بأمان قبل حذف بطاقته فعلياً — بدل تعريضه لتدمير مفاجئ.
- [جديد 4.3] تحليل روابط قائمة الانتظار يعمل الآن بحد أقصى 3 تحليلات
  متوازية في نفس اللحظة؛ أي رابط إضافي يُنسخ قبل انتهاء التحليلات
  الحالية يدخل طابور انتظار داخلي ويبدأ تحليله تلقائياً بمجرد تحرر مكان.
- [جديد 4.3] زر "🗑️ تفريغ القائمة" في نافذة قائمة الانتظار لحذف كل
  الروابط دفعة واحدة، مع رسالة تأكيد قبل التنفيذ.
- [جديد 4.3] خيار جديد في تبويب الإعدادات (قسم "قائمة الانتظار"):
  تفعيل/إلغاء التقاط الروابط تلقائياً من الحافظة إلى قائمة الانتظار،
  والافتراضي مفعّل.

التغييرات الأساسية في النسخة (4.2):
- إصدار البرنامج: 4.2.
- [جديد 4.2] زر "🕒 قائمة الانتظار" في الشاشة الرئيسية: يلتقط تلقائياً أي
  رابط يُنسخ إلى الحافظة أثناء عمل البرنامج، ويحلّله في الخلفية (بلا أي
  تدخل من المستخدم)، ثم يعرضه في نافذة قائمة الانتظار كبطاقة (بنفس تصميم
  بطاقة التحميل) تحوي: العنوان، الصورة، زر نسخ الرابط، زر فتحه في
  المتصفح، قائمة منسدلة بالجودات المتاحة، زر تحميل بالجودة المختارة،
  وزر حذف من القائمة.
- [جديد 4.2] إعادة تسمية شاشة "التحميل المتعدد" إلى "التحميلات".
- [جديد 4.2] أيقونة حذف بطاقة التحميل أصبحت سلة 🗑️ بدل ❌.
- [جديد 4.2] تلميحات الأزرار (Tooltips) أصبحت بخط أسود واضح على خلفية
  فاتحة بدل النص الأبيض غير المقروء.
- [جديد 4.2] إصلاح أيقونة البرنامج: لم تكن تظهر في شريط المهام ولا في
  عنوان النافذة أثناء التشغيل رغم ظهورها على ملف البرنامج نفسه؛ الآن
  يبحث البرنامج عن ملف الأيقونة في عدة مسارات محتملة (مجلد التجميد،
  مجلد التنفيذ، مجلد الملف) ليضمن العثور عليها في كل أوضاع التشغيل.
- [جديد 4.2] تحسين التقاط تنسيقات الروابط "الغريبة" غير المدعومة من
  yt-dlp: فحص أعمق لصفحة الويب (وسوم meta الخاصة بالفيديو، وسوم
  video/source/audio، روابط JSON المُهرّبة بعلامة \\/) بدل الاعتماد فقط
  على روابط الملفات المباشرة داخل HTML الخام.
- [جديد 4.2] إصلاح فقدان بعض التنسيقات في روابط تدعمها yt-dlp فعلياً:
  التنسيقات التي لا يحدد لها yt-dlp كود صوت/فيديو صريحاً (شائع في بعض
  المواقع) لم تكن تظهر إطلاقاً؛ الآن تُعامَل كملف مدمج بدل تجاهلها.

التغييرات الأساسية في النسخة (4.1):
- كل البرنامج في ملف Python واحد بدون استيراد ملفات المشروع الداخلية.
- زر رجوع للرئيسية داخل شاشة التحميل المتعدد.
- تحويل روابط Facebook و SoundCloud تلقائياً من الرئيسية إلى شاشة "تحميل الجميع" مع بدء التحليل.
- تثبيت خياري SD و HD لفيسبوك في التنسيقات المدمجة.
- بطاقات تحميل أصغر وأشيك مع شريط تقدم مختصر ونوع الستريم الحالي (صوت/فيديو) وحجمه.
- تصميم أزرار زجاجي مسطّح هادئ بدل التأثير ثلاثي الأبعاد.
- تحسينات ثبات وسلاسة وإغلاق آمن.
- في شاشة "تحميل الجميع": لو الرابط "غريب" ولم يفهمه yt-dlp، يفحص
  البرنامج صفحة الويب نفسها بحثاً عن أي روابط فيديو/صوت مباشرة (mp4, webm,
  m3u8, mp3, m4a ...) ويضعها في القائمة المناسبة (فيديو مدمج / صوت).
- إصلاح مشكلة "اكتمل التحميل" الوهمية: التحقق الفعلي من نجاح
  yt-dlp (كود الإرجاع) ومن وجود الملف الناتج، والتحقق عبر ffmpeg من احتواء
  الملف على مسار الفيديو والصوت معاً عند التحميل المدمج، بدل افتراض
  النجاح لمجرد عدم حدوث استثناء.
"""

import sys
import os
import re
import json
import hashlib
import subprocess
import glob
import time
import tempfile
import threading
import itertools
import ctypes
from io import BytesIO
from datetime import datetime
from dataclasses import dataclass, field, asdict
from typing import Optional, Dict, List
from http.cookiejar import MozillaCookieJar
from urllib.parse import urljoin, parse_qs, urlparse


# ------------------ مجلد بيانات التطبيق المحلي ------------------ #
def _resolve_app_data_dir() -> str:
    """مجلد محلي قابل للكتابة خاص بالتطبيق حسب نظام التشغيل (يُنشأ عند الحاجة فقط)."""
    app_name = "MGDownloader"
    try:
        if sys.platform.startswith("win"):
            base = os.environ.get("APPDATA") or os.path.expanduser("~")
        elif sys.platform == "darwin":
            base = os.path.join(os.path.expanduser("~"), "Library", "Application Support")
        else:
            base = os.environ.get("XDG_DATA_HOME") or os.path.join(os.path.expanduser("~"), ".local", "share")
        path = os.path.join(base, app_name)
    except Exception:
        path = os.path.join(os.path.abspath("."), f".{app_name}")
    try:
        os.makedirs(path, exist_ok=True)
    except Exception:
        # فشل إنشاء المجلد المفضّل: نرجع لمجلد التشغيل الحالي كحل أخير
        path = os.path.abspath(".")
    return path


APP_DATA_DIR = _resolve_app_data_dir()


def _app_data_path(filename: str) -> str:
    return os.path.join(APP_DATA_DIR, filename)


def _migrate_legacy_file(filename: str):
    """نقل ملف قديم كان يُحفظ بجانب البرنامج (نسخ سابقة) إلى مجلد بيانات التطبيق، إن وُجد ولم يُنقل بعد."""
    try:
        legacy = os.path.join(os.path.abspath("."), filename)
        target = _app_data_path(filename)
        if os.path.exists(legacy) and not os.path.exists(target) and os.path.abspath(legacy) != os.path.abspath(target):
            import shutil
            shutil.copy2(legacy, target)
    except Exception:
        pass


def _secure_file_permissions(path: str):
    """تقييد صلاحيات ملف حساس (مثل الكوكيز) للمستخدم الحالي فقط، حيث يدعمه النظام."""
    try:
        if not sys.platform.startswith("win"):
            os.chmod(path, 0o600)
    except Exception:
        pass


def _atomic_write_text(path: str, text: str, encoding: str = "utf-8"):
    """كتابة آمنة (ذرية) لملف نصي: تُكتب في ملف مؤقت ثم يُستبدل الملف الهدف دفعة واحدة."""
    directory = os.path.dirname(path) or "."
    try:
        os.makedirs(directory, exist_ok=True)
    except Exception:
        pass
    fd, tmp_path = tempfile.mkstemp(prefix=".tmp_", dir=directory)
    try:
        with os.fdopen(fd, "w", encoding=encoding) as f:
            f.write(text)
        os.replace(tmp_path, path)
    except Exception:
        try:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
        except Exception:
            pass
        raise


for _legacy_name in ("settings.json", "yt_cookies.txt", "path.json", "path_merge.json",
                      "download_history.json", "queue_items.json"):
    _migrate_legacy_file(_legacy_name)

# ------------------ سجل الأخطاء (يجب أن يحدث قبل الاستيرادات الكبيرة) ------ #
try:
    log = open(_app_data_path("mylog.txt"), "w", encoding="utf-8")
except Exception:
    try:
        log = open("mylog.txt", "w", encoding="utf-8")
    except Exception:
        log = None


class _Tee:
    def write(self, x):
        try:
            if x and x.strip():
                x = f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {x}"
            if log and not log.closed:
                log.write(x); log.flush()
            if getattr(sys, "frozen", False) is False and sys.__stdout__:
                sys.__stdout__.write(x)
        except Exception:
            pass

    def flush(self):
        try:
            if log and not log.closed:
                log.flush()
        except Exception:
            pass


sys.stdout = sys.stderr = _Tee()


def _global_excepthook(exc_type, exc_value, exc_tb):
    """منع إغلاق البرنامج بلا أثر عند خطأ غير ملتقط: نكتب الخطأ في السجل."""
    try:
        import traceback
        traceback.print_exception(exc_type, exc_value, exc_tb)
    except Exception:
        pass


sys.excepthook = _global_excepthook

# ------------------ المكتبات الخارجية (مع رسالة واضحة عند نقص أي منها) ------ #
_MISSING_DEPS = []


def _require(module_name, pip_name=None, arabic_name=None):
    try:
        return __import__(module_name)
    except Exception:
        _MISSING_DEPS.append(arabic_name or pip_name or module_name)
        return None


_yt_dlp_mod = _require("yt_dlp", arabic_name="yt-dlp")
_requests_mod = _require("requests", arabic_name="requests")
_pyperclip_mod = _require("pyperclip", arabic_name="pyperclip")
_pil_mod = _require("PIL", arabic_name="Pillow")
_imageio_ffmpeg_mod = _require("imageio_ffmpeg", arabic_name="imageio-ffmpeg")
_pyqt6_mod = _require("PyQt6", arabic_name="PyQt6")

if _MISSING_DEPS:
    _msg = (
        "تعذّر تشغيل البرنامج بسبب نقص بعض المكتبات المطلوبة:\n\n"
        + "\n".join(f"  - {d}" for d in _MISSING_DEPS)
        + "\n\nيرجى تثبيتها أولاً، مثال:\n"
        + "pip install " + " ".join(
            {"yt-dlp": "yt-dlp", "requests": "requests", "pyperclip": "pyperclip",
             "Pillow": "Pillow", "imageio-ffmpeg": "imageio-ffmpeg",
             "PyQt6": "PyQt6"}.get(d, d) for d in _MISSING_DEPS
        )
    )
    print(_msg)
    try:
        if log and not log.closed:
            log.write(_msg + "\n")
            log.flush()
    except Exception:
        pass
    sys.exit(1)

import yt_dlp
import requests
import pyperclip
from PIL import Image, ImageDraw
from imageio_ffmpeg import get_ffmpeg_exe

from PyQt6.QtCore import (
    Qt, QSize, QUrl, QObject, QThread, pyqtSignal, QMutex, QMutexLocker, QTimer,
)
from PyQt6.QtGui import (
    QIcon, QFont, QDesktopServices, QPixmap, QImage,
)
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QPushButton, QStackedWidget, QFrame, QButtonGroup, QSizePolicy, QLabel,
    QCheckBox, QFileDialog, QMessageBox, QComboBox, QScrollArea, QProgressBar,
    QSpinBox, QDialog, QListWidget, QListWidgetItem, QDialogButtonBox,
    QTextBrowser,
)

APP_VERSION = "4.3"
APP_VERSION_FULL = "4.3.0.0"
APP_TITLE = "MG Downloader v4.3"

FFMPEG = get_ffmpeg_exe()
COOKIES_FILE = _app_data_path("yt_cookies.txt")
PATHS_FILE = _app_data_path("path.json")             # مسارات الحفظ (فيديو/صوت/قوائم)
HISTORY_FILE = _app_data_path("download_history.json")
CACHE_DIR = _app_data_path("my_cache")
CACHE_INFO_DIR = os.path.join(CACHE_DIR, "information")
CACHE_IMAGES_DIR = os.path.join(CACHE_DIR, "images")
_CREATE_NO_WINDOW = 0
if sys.platform.startswith("win"):
    _CREATE_NO_WINDOW = getattr(subprocess, "CREATE_NO_WINDOW", 0x08000000)


def resource_path(relative_path: str) -> str:
    """مسار صالح في وضع التطوير ومع PyInstaller."""
    try:
        base_path = sys._MEIPASS  # type: ignore[attr-defined]
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def find_app_icon_path(filename: str = "mg.ico") -> str:
    """
    يبحث عن ملف الأيقونة في كل المسارات المحتملة حسب طريقة التشغيل.
    السبب: كانت الأيقونة تظهر على ملف البرنامج نفسه (لأنها مُضمَّنة داخل
    الـ exe عبر PyInstaller --icon) لكنها لا تظهر في شريط المهام ولا في
    عنوان النافذة أثناء التشغيل، لأن resource_path() القديمة كانت تبحث في
    مسار واحد فقط (_MEIPASS أو مجلد التشغيل الحالي)؛ لو لم يكن الملف هناك
    (مثلاً في وضع onedir حيث يوضع بجانب الـ exe لا داخل _MEIPASS، أو عند
    التشغيل من مسار عمل مختلف) لم تُطبَّق QIcon على النافذة إطلاقاً.
    """
    candidates = []
    try:
        candidates.append(os.path.join(sys._MEIPASS, filename))  # type: ignore[attr-defined]
    except Exception:
        pass
    try:
        if getattr(sys, "frozen", False):
            candidates.append(os.path.join(os.path.dirname(sys.executable), filename))
    except Exception:
        pass
    try:
        candidates.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), filename))
    except Exception:
        pass
    candidates.append(os.path.join(os.path.abspath("."), filename))

    for path in candidates:
        try:
            if path and os.path.exists(path):
                return path
        except Exception:
            continue
    # لم يُعثر على الملف في أي مسار معروف
    return ""


def _norm_url(url: str) -> str:
    return (url or "").strip().split()[0] if url else ""


def _is_valid_url(url: str) -> bool:
    url = _norm_url(url)
    return url.startswith("http://") or url.startswith("https://")


def _is_facebook_url(url: str) -> bool:
    u = (url or "").lower()
    return any(d in u for d in ("facebook.com", "fb.watch", "fb.com", "m.facebook.com", "web.facebook.com"))


def _is_soundcloud_url(url: str) -> bool:
    return "soundcloud.com" in (url or "").lower()


def _is_force_platform(url: str) -> bool:
    return _is_facebook_url(url) or _is_soundcloud_url(url)


def _looks_like_playlist_url(url: str) -> bool:
    """التعرّف على روابط القوائم قبل عرض نتيجة التحليل كفشل عادي."""
    raw = (url or "").strip().lower()
    if not raw:
        return False
    try:
        parsed = urlparse(raw)
        query = parse_qs(parsed.query)
        if any(key in query for key in ("list", "playlist", "collection", "album")):
            return True
        path = parsed.path or ""
    except Exception:
        path = raw
    return any(marker in path for marker in ("/playlist", "/playlists", "/collection/", "/album/"))


def _facebook_video_output_path(directory: str, base_name: str, extension: str = ".mp4") -> str:
    """إنشاء مسار Facebook فريد باسم الفيديو وتاريخ/وقت التحميل."""
    extension = extension if extension.startswith(".") else f".{extension}"
    stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
    stem = f"{base_name}_{stamp}"
    candidate = os.path.join(directory, f"{stem}{extension}")
    counter = 2
    while os.path.exists(candidate):
        candidate = os.path.join(directory, f"{stem}_{counter}{extension}")
        counter += 1
    return candidate


# ------------------ فحص يدوي لصفحة ويب "غريبة" عن روابط ميديا مباشرة ------------------ #
# تُستخدم في شاشة "تحميل الجميع" عندما يفشل yt-dlp في فهم الرابط (رابط غريب/غير مدعوم):
# نجلب صفحة الويب ونبحث نصياً عن أي روابط فيديو أو صوت مباشرة ونضعها في المكان المناسب.
_MEDIA_VIDEO_EXTS = (".mp4", ".webm", ".mkv", ".mov", ".m4v", ".avi", ".flv", ".ts", ".m3u8", ".mpd")
_MEDIA_AUDIO_EXTS = (".mp3", ".m4a", ".wav", ".ogg", ".oga", ".flac", ".aac", ".wma", ".opus")

# روابط ميديا مباشرة داخل نص الصفحة (HTML/JS)، بما فيها JSON مُهرَّب بعلامة \/
_MEDIA_LINK_RE = re.compile(
    r"""["'(]\s*([^"'()\s]+\.(?:mp4|webm|mkv|mov|m4v|avi|flv|ts|m3u8|mpd|mp3|m4a|wav|ogg|oga|flac|aac|wma|opus))"""
    r"""(?:[?#][^"'()\s]*)?["')]""",
    re.IGNORECASE,
)
# وسوم <video>/<source>/<audio> ووسوم meta الخاصة بمشغلات الفيديو (og:video، twitter:player إلخ)
_MEDIA_TAG_RE = re.compile(
    r"""<(?:source|video|audio)[^>]+src\s*=\s*["']([^"']+)["']""",
    re.IGNORECASE,
)
_MEDIA_META_RE = re.compile(
    r"""<meta[^>]+(?:property|name)\s*=\s*["'](?:og:video(?::url|:secure_url)?"""
    r"""|twitter:player:stream|og:audio(?::url|:secure_url)?)["'][^>]+content\s*=\s*["']([^"']+)["']""",
    re.IGNORECASE,
)
_TITLE_TAG_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)


def _unescape_json_url(raw: str) -> str:
    """يفكّ تهريب سلاسل JSON الشائعة (\\/ → / و \\u0026 → &) داخل رابط مُستخرج نصياً."""
    try:
        return raw.replace("\\/", "/").replace("\\u0026", "&")
    except Exception:
        return raw

_GENERIC_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)


def _probe_remote_size(url: str, headers: dict) -> float:
    """محاولة معرفة حجم ملف بعيد (MB) عبر HEAD، ثم GET جزئي (Range) كحل بديل."""
    try:
        r = requests.head(url, headers=headers, timeout=10, allow_redirects=True)
        length = r.headers.get("Content-Length")
        if length and length.isdigit():
            return round(int(length) / (1024 * 1024), 2)
    except Exception:
        pass
    try:
        h2 = dict(headers)
        h2["Range"] = "bytes=0-0"
        r = requests.get(url, headers=h2, timeout=10, stream=True)
        cr = r.headers.get("Content-Range", "")
        try:
            r.close()
        except Exception:
            pass
        if "/" in cr:
            total = cr.split("/")[-1].strip()
            if total.isdigit():
                return round(int(total) / (1024 * 1024), 2)
    except Exception:
        pass
    return 0.0


def _scan_page_for_media(url: str):
    """
    فحص صفحة ويب (رابط لا يفهمه yt-dlp) بحثاً عن أي روابط فيديو/صوت مباشرة
    داخل كود الصفحة (HTML/JS)، وإرجاعها بشكل متوافق مع information_force:
    (audio: dict, video_audio: dict, info: [title, duration, thumbnail]).
    """
    headers = {"User-Agent": _GENERIC_UA, "Accept": "*/*"}
    try:
        resp = requests.get(url, headers=headers, timeout=20)
        resp.raise_for_status()
        html = resp.text
        page_url = resp.url or url
    except Exception as e:
        print(f"[generic] فشل جلب الصفحة للبحث اليدوي عن الميديا: {e}")
        return {}, {}, ["untitled", 0, ""]

    found = []
    seen = set()

    def _collect(raw: str):
        raw = _unescape_json_url((raw or "").strip())
        if not raw:
            return
        try:
            full = urljoin(page_url, raw)
        except Exception:
            return
        if full in seen:
            return
        seen.add(full)
        found.append(full)

    # 1) روابط منتهية بامتداد ميديا داخل أي نص/JSON في الصفحة
    for m in _MEDIA_LINK_RE.finditer(html):
        _collect(m.group(1))
    # 2) وسوم <video>/<source>/<audio> — حتى بلا امتداد صريح بآخر الرابط
    for m in _MEDIA_TAG_RE.finditer(html):
        _collect(m.group(1))
    # 3) وسوم meta الخاصة بمشغلات الفيديو (og:video، twitter:player:stream ...)
    for m in _MEDIA_META_RE.finditer(html):
        _collect(m.group(1))

    title = "untitled"
    tm = _TITLE_TAG_RE.search(html)
    if tm:
        title = re.sub(r"\s+", " ", tm.group(1)).strip() or "untitled"

    audio = {}
    video_audio = {}
    ac = vc = 0
    for link in found:
        ext = os.path.splitext(link.split("?")[0].split("#")[0])[1].lower()
        is_audio_ext = ext in _MEDIA_AUDIO_EXTS
        is_video_ext = ext in _MEDIA_VIDEO_EXTS
        if not is_audio_ext and not is_video_ext:
            # لا يوجد امتداد معروف بآخر الرابط (شائع في روابط <video src=...>
            # أو meta[og:video] التي تُخرج عبر سكريبت مباشر بلا امتداد بالمسار)؛
            # نتحقق من نوع المحتوى الفعلي عبر رأس Content-Type بدل تجاهل الرابط.
            ctype = ""
            try:
                r = requests.head(link, headers=headers, timeout=8, allow_redirects=True)
                ctype = (r.headers.get("Content-Type") or "").lower()
            except Exception:
                ctype = ""
            if ctype.startswith("video/") or "mpegurl" in ctype or "dash+xml" in ctype:
                is_video_ext = True
            elif ctype.startswith("audio/"):
                is_audio_ext = True
            else:
                continue
        size_mb = _probe_remote_size(link, headers)
        if is_audio_ext:
            audio[ac] = [0, f"direct:{link}", size_mb]
            ac += 1
        else:
            label = ext.lstrip(".").upper() or "MEDIA"
            video_audio[vc] = [label, f"direct:{link}", size_mb]
            vc += 1

    return audio, video_audio, [title, 0, ""]


SETTINGS_FILE = _app_data_path("settings.json")
QUEUE_FILE = _app_data_path("queue_items.json")

_DEFAULTS = {
    "main": {
        "high_audio": False,
        "high_video": False,
        "subtitle": False,
        "subtitle_lang": "ar",
        "cookies": False,
    },
    "force": {
        "subtitle": False,
        "subtitle_lang": "ar",
        "cookies": False,
    },
    "list": {
        "high_audio": False,
        "high_video": False,
        "subtitle": False,
        "subtitle_lang": "ar",
        "cookies": False,
    },
    "downloads": {
        "max_parallel": 3,
        "auto_switch": False,
    },
    "queue": {
        "capture_enabled": True,
        "width": 660,
        "height": 540,
    },
    "settings": {
        "cookies_browser": "تلقائي",
    },
    "functions": {
        "bitrate": "48k",
        "channels": "2",
    },
}


def _deep_merge(base, override):
    """دمج عميق: قيم override تتغلب لكن نُبقي مفاتيح base غير الموجودة."""
    if not isinstance(override, dict):
        return base
    result = dict(base)
    for k, v in override.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = _deep_merge(result[k], v)
        else:
            result[k] = v
    return result


def load_settings() -> dict:
    """قراءة الإعدادات من القرص (مع defaults للقيم المفقودة)."""
    try:
        if not os.path.exists(SETTINGS_FILE):
            return json.loads(json.dumps(_DEFAULTS))  # نسخة عميقة
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            return json.loads(json.dumps(_DEFAULTS))
        return _deep_merge(_DEFAULTS, data)
    except Exception as e:
        print(f"[settings] خطأ قراءة الإعدادات: {e}")
        return json.loads(json.dumps(_DEFAULTS))


def save_settings(data: dict):
    """حفظ الإعدادات إلى القرص بطريقة آمنة (ذرية)."""
    try:
        _atomic_write_text(SETTINGS_FILE, json.dumps(data, ensure_ascii=False, indent=2))
    except Exception as e:
        print(f"[settings] خطأ حفظ الإعدادات: {e}")


def get_section(section: str) -> dict:
    """قراءة قسم معين فقط."""
    data = load_settings()
    return data.get(section, dict(_DEFAULTS.get(section, {})))


def update_section(section: str, updates: dict):
    """تحديث قسم معين وحفظ."""
    data = load_settings()
    if section not in data or not isinstance(data[section], dict):
        data[section] = dict(_DEFAULTS.get(section, {}))
    data[section].update(updates or {})
    save_settings(data)


def update_value(section: str, key: str, value):
    """تحديث قيمة واحدة في قسم معين وحفظ."""
    update_section(section, {key: value})


# ألوان الثيم
COLOR_BG_DARK = "#252422"
COLOR_BG_DARKER = "#1E1E21"
COLOR_BG_PANEL = "#3A3A40"
COLOR_BG_PANEL_LIGHT = "#4A4A52"
COLOR_BG_HOVER = "#52525A"
COLOR_BG_PRESSED = "#1A1A1D"
COLOR_ACCENT_BLUE = "#3A6EA5"
COLOR_ACCENT_BLUE_LIGHT = "#5A8EC5"
COLOR_ACCENT_BLUE_DARK = "#1A4E85"
COLOR_ACCENT_GREEN = "#077542"
COLOR_ACCENT_GREEN_LIGHT = "#0A9555"
COLOR_ACCENT_GREEN_DARK = "#055530"
COLOR_TEXT = "#FFFFFF"
COLOR_TEXT_DIM = "#B0B0B0"
COLOR_BORDER = "#1A1A1D"
COLOR_BORDER_LIGHT = "#5A5A60"

# ألوان تناوب الجودات
COLOR_ALT_A = "#2B2B2E"
COLOR_ALT_B = "#1E1E21"


QSS = f"""
* {{
    font-family: "Arial", "Tahoma", sans-serif;
    font-size: 18px;
    color: {COLOR_TEXT};
}}

QMainWindow, QWidget {{
    background-color: {COLOR_BG_DARK};
    font-family: "Arial";
    font-size: 18px;
}}

QFrame#TopBar {{
    background-color: rgba(30, 30, 33, 0.92);
    border-bottom: 1px solid rgba(255, 255, 255, 0.06);
}}

/* ================== أزرار زجاجية هادئة (تصميم مسطّح خفيف) ================== */
QPushButton {{
    background-color: rgba(255, 255, 255, 0.06);
    color: {COLOR_TEXT};
    border: 1px solid rgba(255, 255, 255, 0.10);
    border-radius: 10px;
    padding: 7px 12px;
    font-weight: bold;
    font-family: "Arial";
    font-size: 18px;
}}

QPushButton:hover {{
    background-color: rgba(255, 255, 255, 0.11);
    border: 1px solid rgba(255, 255, 255, 0.18);
}}

QPushButton:pressed {{
    background-color: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.08);
}}

QPushButton:disabled {{
    background-color: rgba(255, 255, 255, 0.03);
    color: #5A5A5A;
    border: 1px solid rgba(255, 255, 255, 0.05);
}}

/* أزرار التبويبات في الشريط العلوي - زجاجي مسطّح */
QPushButton#TabButton {{
    background-color: transparent;
    border: none;
    border-bottom: 2px solid transparent;
    border-radius: 0px;
    padding: 8px 14px;
    font-size: 20px;
    font-weight: bold;
    color: {COLOR_TEXT};
    font-family: "Arial";
}}

QPushButton#TabButton:hover {{
    background-color: rgba(255, 255, 255, 0.06);
}}

QPushButton#TabButton:checked {{
    background-color: rgba(90, 142, 197, 0.12);
    border-bottom: 2px solid {COLOR_ACCENT_BLUE_LIGHT};
    color: {COLOR_ACCENT_BLUE_LIGHT};
}}

/* الزر الرئيسي (التحليل/التحميل) - زجاجي أزرق هادئ */
QPushButton#PrimaryButton {{
    background-color: rgba(90, 142, 197, 0.28);
    border: 1px solid rgba(90, 142, 197, 0.55);
    border-radius: 12px;
    font-size: 25px;
    font-weight: bold;
    padding: 12px 16px;
    color: white;
    font-family: "Arial";
}}

QPushButton#PrimaryButton:hover {{
    background-color: rgba(90, 142, 197, 0.40);
    border: 1px solid rgba(90, 142, 197, 0.75);
}}

QPushButton#PrimaryButton:pressed {{
    background-color: rgba(90, 142, 197, 0.20);
}}

QPushButton#PrimaryButton:disabled {{
    background-color: rgba(90, 142, 197, 0.08);
    color: #6A7A8A;
    border: 1px solid rgba(90, 142, 197, 0.15);
}}

/* زر النجاح (دمج/ترميز) - زجاجي أخضر هادئ */
QPushButton#SuccessButton {{
    background-color: rgba(10, 149, 85, 0.28);
    border: 1px solid rgba(10, 149, 85, 0.55);
    border-radius: 12px;
    font-size: 22px;
    font-weight: bold;
    padding: 9px 12px;
    color: white;
    font-family: "Arial";
}}

QPushButton#SuccessButton:hover {{
    background-color: rgba(10, 149, 85, 0.40);
    border: 1px solid rgba(10, 149, 85, 0.75);
}}

QPushButton#SuccessButton:pressed {{
    background-color: rgba(10, 149, 85, 0.20);
}}

/* أزرار الجودات - زجاجي هادئ */
QPushButton#QualityButton {{
    background-color: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.10);
    border-radius: 10px;
    font-size: 20px;
    font-weight: bold;
    padding: 9px 10px;
    text-align: right;
    font-family: "Arial";
}}

QPushButton#QualityButton:hover {{
    background-color: rgba(255, 255, 255, 0.11);
    border: 1px solid rgba(255, 255, 255, 0.18);
}}

QPushButton#QualityButton:pressed {{
    background-color: rgba(255, 255, 255, 0.04);
}}

QPushButton#QualityButton:disabled {{
    background-color: rgba(255, 255, 255, 0.03);
    color: #5A5A5A;
    border: 1px solid rgba(255, 255, 255, 0.05);
}}

QPushButton#QualityActive {{
    background-color: rgba(10, 149, 85, 0.32);
    border: 1px solid rgba(10, 149, 85, 0.65);
    border-radius: 10px;
    font-size: 20px;
    font-weight: bold;
    padding: 9px 10px;
    text-align: right;
    color: white;
    font-family: "Arial";
}}

/* مدخلات */
QLineEdit, QComboBox, QSpinBox {{
    background-color: rgba(255, 255, 255, 0.05);
    color: {COLOR_TEXT};
    border: 1px solid rgba(255, 255, 255, 0.10);
    border-radius: 8px;
    padding: 5px 8px;
    selection-background-color: {COLOR_ACCENT_BLUE};
    font-family: "Arial";
    font-size: 16px;
}}

QComboBox::drop-down {{
    border: none;
    width: 24px;
}}

QComboBox QAbstractItemView {{
    background-color: {COLOR_BG_PANEL};
    color: {COLOR_TEXT};
    selection-background-color: {COLOR_ACCENT_BLUE};
    border: 1px solid rgba(255, 255, 255, 0.10);
    font-family: "Arial";
}}

/* مربعات الاختيار */
QCheckBox {{
    color: {COLOR_TEXT};
    spacing: 6px;
    font-weight: bold;
    font-family: "Arial";
    font-size: 16px;
}}

QCheckBox::indicator {{
    width: 18px;
    height: 18px;
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 5px;
    background-color: rgba(255, 255, 255, 0.05);
}}

QCheckBox::indicator:checked {{
    background-color: rgba(90, 142, 197, 0.55);
    border: 1px solid {COLOR_ACCENT_BLUE_LIGHT};
}}

/* شريط التقدم - مسطّح هادئ */
QProgressBar {{
    background-color: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.10);
    border-radius: 9px;
    text-align: center;
    color: {COLOR_TEXT};
    font-weight: bold;
    font-family: "Arial";
    height: 20px;
}}

QProgressBar::chunk {{
    background-color: rgba(90, 142, 197, 0.65);
    border-radius: 7px;
}}

/* شريط التمرير */
QScrollBar:vertical {{
    background: transparent;
    width: 12px;
    border-radius: 6px;
}}

QScrollBar::handle:vertical {{
    background: rgba(255, 255, 255, 0.14);
    border-radius: 6px;
    min-height: 30px;
}}

QScrollBar::handle:vertical:hover {{
    background: rgba(90, 142, 197, 0.45);
}}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
    height: 0px;
}}

QScrollBar:horizontal {{
    background: transparent;
    height: 12px;
    border-radius: 6px;
}}

QScrollBar::handle:horizontal {{
    background: rgba(255, 255, 255, 0.14);
    border-radius: 6px;
    min-width: 30px;
}}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{
    width: 0px;
}}

/* بطاقات التحميل - زجاجي مسطّح هادئ */
QFrame#DownloadCard {{
    background-color: rgba(255, 255, 255, 0.045);
    border: 1px solid rgba(255, 255, 255, 0.10);
    border-radius: 12px;
}}

QFrame#DownloadCard[status="done"] {{
    border: 1px solid rgba(10, 149, 85, 0.55);
}}

QFrame#DownloadCard[status="error"] {{
    border: 1px solid rgba(192, 64, 64, 0.55);
}}

QFrame#DownloadCard[status="paused"] {{
    border: 1px solid rgba(176, 132, 10, 0.55);
}}



QProgressBar#CompactProgress {{
    min-height: 16px;
    max-height: 16px;
    border-radius: 8px;
    font-size: 12px;
}}

QProgressBar#CompactProgress::chunk {{
    border-radius: 7px;
}}

QLabel#StatusChip {{
    background-color: rgba(255, 255, 255, 0.06);
    color: #D7E9FF;
    border: 1px solid rgba(90, 142, 197, 0.45);
    border-radius: 8px;
    padding: 3px 9px;
    font-size: 14px;
    font-weight: bold;
}}

QLabel#StreamSizeLabel {{
    background-color: rgba(90, 142, 197, 0.14);
    color: #BFE2FF;
    border: 1px solid rgba(90, 142, 197, 0.35);
    border-radius: 8px;
    padding: 3px 8px;
    font-size: 14px;
    font-weight: bold;
}}

QLabel {{
    color: {COLOR_TEXT};
    background: transparent;
    font-family: "Arial";
}}

QLabel#TitleLabel {{
    background-color: rgba(90, 142, 197, 0.16);
    color: {COLOR_TEXT};
    border: 1px solid rgba(90, 142, 197, 0.35);
    border-radius: 12px;
    padding: 8px;
    font-size: 23px;
    font-weight: bold;
    font-family: "Arial";
}}

QLabel#PathLabel {{
    background-color: rgba(255, 255, 255, 0.07);
    color: {COLOR_TEXT};
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 8px;
    padding: 3px 8px;
    font-weight: bold;
    font-family: "Arial";
}}

/* الفريمات الداخلية - زجاجي مسطّح خفيف */
QFrame#Panel {{
    background-color: rgba(255, 255, 255, 0.035);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 12px;
}}

QFrame#PanelDark {{
    background-color: rgba(0, 0, 0, 0.18);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 12px;
}}

QMessageBox {{
    background-color: {COLOR_BG_DARK};
    font-family: "Arial";
}}

QMessageBox QLabel {{
    color: {COLOR_TEXT};
    font-family: "Arial";
    font-size: 16px;
}}

/* تلميحات الأزرار (Tooltips) - خط أسود واضح على خلفية فاتحة بدل النص
   الأبيض الموروث من قاعدة `* {{ color: ... }}` والذي كان يجعلها غير مقروءة */
QToolTip {{
    background-color: #F5F1E8;
    color: #111111;
    border: 1px solid rgba(0, 0, 0, 0.35);
    border-radius: 6px;
    padding: 4px 8px;
    font-family: "Arial";
    font-size: 14px;
    font-weight: bold;
}}
"""


def apply_theme(app):
    """تطبيق ثيم QSS مركزي على التطبيق + خط Arial 13pt (≈ 18px)."""
    app.setStyleSheet(QSS)
    f = QFont("Arial", 13)
    f.setStyleStrategy(QFont.StyleStrategy.PreferAntialias)
    app.setFont(f)


# قائمة المتصفحات حسب الأولوية
_BROWSERS = ("chrome", "edge", "brave", "firefox", "opera", "chromium", "vivaldi")


def _extract_via_api(browser: str) -> bool:
    """
    استخراج الكوكيز عبر API الداخلي لـ yt-dlp وكتابتها بصيغة Netscape.
    تُرجع True عند النجاح.
    """
    try:
        from yt_dlp.cookies import extract_cookies_from_browser
    except Exception as e:
        print(f"[cookies] API غير متاح: {e}")
        return False

    try:
        # extract_cookies_from_browser يستقبل (browser_name, profile=None, keyring=None,
        # container=None, logger=...) — التواقيع تختلف بين الإصدارات؛ نمرّر اسم
        # المتصفح فقط ونستخدم defaults.
        jar = extract_cookies_from_browser(browser)
    except TypeError:
        # تواقيع أقدم
        try:
            jar = extract_cookies_from_browser(browser, None)
        except Exception as e:
            print(f"[cookies] فشل استخراج {browser}: {e}")
            return False
    except Exception as e:
        print(f"[cookies] فشل استخراج {browser}: {e}")
        return False

    if jar is None:
        return False

    try:
        # حول إلى MozillaCookieJar (صيغة Netscape) واحفظ
        mcj = MozillaCookieJar(COOKIES_FILE)
        # نسخ الكوكيز من jar إلى mcj
        for c in jar:
            try:
                mcj.set_cookie(c)
            except Exception:
                pass
        mcj.save(ignore_discard=True, ignore_expires=True)
        _secure_file_permissions(COOKIES_FILE)
    except Exception as e:
        print(f"[cookies] فشل كتابة الملف من {browser}: {e}")
        return False

    if os.path.exists(COOKIES_FILE) and os.path.getsize(COOKIES_FILE) > 100:
        # نتأكد أن الملف ليس صفحة فارغة فقط
        try:
            with open(COOKIES_FILE, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            # نتحقق من وجود سطر كوكي يوتيوب حقيقي
            if "youtube.com" in content or "google.com" in content:
                return True
        except Exception:
            pass
    return False


def _extract_via_cli(browser: str) -> bool:
    """
    احتياطي: استدعاء yt-dlp CLI مع --cookies-from-browser لإنتاج الملف.
    """
    cmd = [
        sys.executable, "-m", "yt_dlp",
        "--cookies-from-browser", browser,
        "--cookies", COOKIES_FILE,
        "--skip-download",
        "--quiet",
        "--no-warnings",
        # رابط خفيف لإجبار yt-dlp على تحميل الكوكيز
        "https://www.youtube.com/",
    ]
    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=60,
            creationflags=_CREATE_NO_WINDOW,
        )
        if result.returncode == 0 and os.path.exists(COOKIES_FILE) \
                and os.path.getsize(COOKIES_FILE) > 100:
            _secure_file_permissions(COOKIES_FILE)
            return True
        err = (result.stderr or b"").decode(errors="ignore")[:400]
        if err.strip():
            print(f"[cookies] CLI {browser}: {err.strip()}")
        return False
    except subprocess.TimeoutExpired:
        print(f"[cookies] CLI {browser}: timeout")
        return False
    except Exception as e:
        print(f"[cookies] CLI {browser}: {e}")
        return False


def refresh_cookies(preferred_browser: str = None) -> bool:
    """
    تحديث ملف الكوكيز yt_cookies.txt من أحد المتصفحات المتاحة.
    :param preferred_browser: لو محدد، نُجرّبه أولاً (chrome/edge/firefox/...).
    :return: True عند النجاح وإلا False.
    """
    # احذف الملف القديم لو فاسد
    try:
        if os.path.exists(COOKIES_FILE) and os.path.getsize(COOKIES_FILE) < 50:
            os.remove(COOKIES_FILE)
    except Exception:
        pass

    browsers = list(_BROWSERS)
    if preferred_browser and preferred_browser in browsers:
        browsers.remove(preferred_browser)
        browsers.insert(0, preferred_browser)

    for browser in browsers:
        print(f"[cookies] محاولة استخراج من {browser}...")
        # 1) جرّب الـ API الداخلي أولاً
        if _extract_via_api(browser):
            print(f"[cookies] ✅ تم التجديد من {browser} (API).")
            return True
        # 2) لو فشل، جرّب CLI
        if _extract_via_cli(browser):
            print(f"[cookies] ✅ تم التجديد من {browser} (CLI).")
            return True

    print("[cookies] ❌ تعذّر تجديد الكوكيز من أي متصفح متاح.")
    return False


def _format_time(seconds: float) -> str:
    if seconds < 0:
        seconds = 0
    total_ms = round(seconds * 1000)
    ms = int(total_ms % 1000)
    total_seconds = int(total_ms // 1000)
    s = total_seconds % 60
    m = (total_seconds // 60) % 60
    h = total_seconds // 3600
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def _fix_overlap(transcript):
    fixed = []
    prev_text = ""
    for i, entry in enumerate(transcript):
        text = entry['text'].strip()
        if not text or text == prev_text:
            continue
        start = entry['start']
        if i < len(transcript) - 1:
            end = transcript[i + 1]['start']
        else:
            end = start + entry['duration']
        if end <= start:
            end = start + 0.5
        fixed.append({'start': start, 'end': end, 'text': text})
        prev_text = text
    return fixed


def _json3_to_srt(json_path: str, srt_path: str) -> bool:
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"[subtitle] فشل قراءة {json_path}: {e}")
        return False

    transcript = []
    for event in data.get('events', []):
        if 'segs' not in event:
            continue
        text = ''.join(seg.get('utf8', '') for seg in event['segs']).strip()
        if not text:
            continue
        transcript.append({
            'start': event.get('tStartMs', 0) / 1000,
            'duration': event.get('dDurationMs', 0) / 1000,
            'text': text,
        })

    if not transcript:
        return False

    fixed = _fix_overlap(transcript)
    try:
        os.makedirs(os.path.dirname(srt_path) or ".", exist_ok=True)
        with open(srt_path, 'w', encoding='utf-8') as f:
            for i, line in enumerate(fixed, 1):
                f.write(f"{i}\n")
                f.write(f"{_format_time(line['start'])} --> {_format_time(line['end'])}\n")
                f.write(f"{line['text']}\n\n")
        return True
    except Exception as e:
        print(f"[subtitle] فشل كتابة SRT: {e}")
        return False


def _try_yt_dlp(url, outtmpl, langs, mode, cookies=None, attempts=2):
    """
    mode: 'manual' = writesubtitles فقط، 'auto' = writeautomaticsub فقط، 'both' = الاثنان.
    تُرجع قائمة ملفات json3 الناتجة في out_dir (قد تكون فارغة).
    """
    opts = {
        'quiet': True,
        'no_warnings': True,
        'skip_download': True,
        'writesubtitles': mode in ('manual', 'both'),
        'writeautomaticsub': mode in ('auto', 'both'),
        'subtitleslangs': list(langs),
        'subtitlesformat': 'json3',
        'outtmpl': outtmpl,
        'sleep_interval': 2,
        'max_sleep_interval': 5,
        'retries': 2,
        'ignoreerrors': True,
    }
    if cookies and os.path.exists(cookies):
        opts['cookies'] = cookies

    out_dir = os.path.dirname(outtmpl) or "."
    delay = 5
    for attempt in range(1, attempts + 1):
        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                ydl.extract_info(url, download=True)
            files = glob.glob(os.path.join(out_dir, "*.json3"))
            if files:
                return files
            print(f"[subtitle] mode={mode} langs={langs} attempt={attempt}: لا json3.")
        except yt_dlp.utils.DownloadError as de:
            msg = str(de)
            if "429" in msg or "Too Many Requests" in msg:
                print(f"[subtitle] HTTP 429 — انتظار {delay}s...")
                time.sleep(delay)
                delay = min(delay * 2, 60)
                continue
            print(f"[subtitle] DownloadError: {de}")
            return []
        except Exception as e:
            print(f"[subtitle] خطأ غير متوقع: {e}")
            return []
        time.sleep(delay)
        delay = min(delay * 2, 60)
    return []


def _pick_best_json(json_files, prefer_lang):
    """اختر أنسب ملف json3 من القائمة (يحتوي على prefer_lang في الاسم)."""
    if not json_files:
        return None
    pl = prefer_lang.lower()
    # الأولوية: الذي اسمه يحتوي .{prefer_lang}.
    for jf in json_files:
        base = os.path.basename(jf).lower()
        if f".{pl}." in base:
            return jf
    # ثم الذي يبدأ بـ {prefer_lang} (مثل ar-EG, ar.json3)
    for jf in json_files:
        base = os.path.basename(jf).lower()
        if pl in base:
            return jf
    # وإلا أول واحد
    return json_files[0]


def _fetch_lang(url, tmpdir, lang, cookies):
    """
    حاول جلب ترجمة بلغة معينة: يدوية أولاً ثم آلية ثم variants.
    تُرجع مسار ملف json3 الذي يُفضَّل أو None.
    """
    outtmpl = os.path.join(tmpdir, f"subs_{lang}")
    # 1) variants أساسية + يدوية + آلية معاً
    langs_main = [lang, f"{lang}.*"]

    # محاولة 1: يدوية فقط
    files = _try_yt_dlp(url, outtmpl, langs_main, mode='manual', cookies=cookies, attempts=2)
    chosen = _pick_best_json(files, lang)
    if chosen:
        return chosen, "manual"

    # امسح أي بقايا
    for f in glob.glob(os.path.join(tmpdir, "subs_*.json3")):
        try:
            os.remove(f)
        except Exception:
            pass

    # محاولة 2: آلية فقط
    files = _try_yt_dlp(url, outtmpl, langs_main, mode='auto', cookies=cookies, attempts=2)
    chosen = _pick_best_json(files, lang)
    if chosen:
        return chosen, "auto"

    # نظف أيضاً
    for f in glob.glob(os.path.join(tmpdir, "subs_*.json3")):
        try:
            os.remove(f)
        except Exception:
            pass

    return None, None


def download_and_fix_subtitle(url: str, video_path: str, lang: str = "ar"):
    """
    تحميل ترجمة بلغة محددة (ar أو en) للفيديو.
    - يجرّب اللغة المطلوبة (يدوية → آلية).
    - لو فشل، يجرّب اللغة الأخرى احتياطياً.
    - الملف الناتج بنفس اسم الفيديو بالضبط (مثل: video.srt) ليتشغّل تلقائياً
      مع مشغّلات الفيديو.
    """
    if lang not in ("ar", "en"):
        lang = "ar"
    fallback = "en" if lang == "ar" else "ar"

    video_dir = os.path.dirname(video_path) or "."
    # نأخذ اسم الفيديو بدون الامتداد، مع مراعاة أن yt-dlp قد ينتج .mkv بدل .mp4
    video_base = os.path.splitext(os.path.basename(video_path))[0]

    # اسم SRT النهائي = نفس اسم الفيديو بدون لاحقة لغة (يفتح تلقائياً بمشغلات الفيديو)
    srt_path = os.path.join(video_dir, f"{video_base}.srt")

    cookies = "yt_cookies.txt"
    chosen_json = None
    chosen_source = None

    with tempfile.TemporaryDirectory() as tmpdir:
        # المحاولة الأولى: اللغة المطلوبة
        print(f"[subtitle] محاولة جلب اللغة: {lang}")
        chosen_json, chosen_source = _fetch_lang(url, tmpdir, lang, cookies)

        # إن فشلت، جرّب اللغة الأخرى
        if not chosen_json:
            print(f"[subtitle] لم تتوفر '{lang}'، تجربة الاحتياطي: {fallback}")
            time.sleep(3)
            chosen_json, chosen_source = _fetch_lang(url, tmpdir, fallback, cookies)

        if not chosen_json:
            print("[subtitle] لا توجد ترجمة متاحة بأي لغة.")
            return []

        print(f"[subtitle] استُخدم الملف: {os.path.basename(chosen_json)} "
              f"(مصدر: {chosen_source})")

        if _json3_to_srt(chosen_json, srt_path):
            print(f"[subtitle] تم إنشاء: {srt_path}")
            return [srt_path]

    print("[subtitle] فشل تحويل json3 إلى SRT.")
    return []


def default_downloads_dir():
    """مسار التحميلات الافتراضي للمستخدم الحالي بشكل متعدد المنصات."""
    return os.path.join(os.path.expanduser("~"), "Downloads")


class StopDownload(Exception):
    """استثناء لإيقاف/إلغاء التحميل من قِبل المستخدم."""
    pass


class YouTubeDownloader:
    def __init__(self):
        self.name_image = ""
        self.path = ""
        downloads = default_downloads_dir()
        self.path_audio = downloads
        self.path_video = downloads
        self.bool_path = False

        self.id = []
        self.name = ""
        self.youtube_audio_qualities = {}
        self.youtube_video_qualities = {}
        self.bool_dict_info = False
        self.info_url = {}

        self._create_directories()

    def _create_directories(self):
        """إنشاء مجلدات الكاش الضرورية."""
        for directory in (CACHE_INFO_DIR, CACHE_IMAGES_DIR):
            if not os.path.exists(directory):
                os.makedirs(directory, exist_ok=True)

    # ------------------------------------------------------------------ #
    def clean_filename(self, name):
        """تنظيف اسم الملف من الإيموجي والرموز الممنوعة، يبقي العربي/الإنجليزي/الأرقام."""
        if not name:
            return "untitled"
        emoji_pattern = re.compile(
            "["
            "\\U0001F600-\\U0001F64F"
            "\\U0001F300-\\U0001F5FF"
            "\\U0001F680-\\U0001F6FF"
            "\\U0001F1E0-\\U0001F1FF"
            "\\U00002702-\\U000027B0"
            "\\U000024C2-\\U0001F251"
            "\\U0001f926-\\U0001f937"
            "\\U00010000-\\U0010ffff"
            "\\u2640-\\u2642"
            "\\u2600-\\u2B55"
            "\\u200d"
            "\\u23cf"
            "\\u23e9"
            "\\u231a"
            "\\ufe0f"
            "\\u3030"
            "]+",
            flags=re.UNICODE,
        )
        name = emoji_pattern.sub('', name)
        # إبقاء العربي والإنجليزي والأرقام والمسافة فقط
        name = re.sub(
            r'[^a-zA-Z0-9\u0600-\u06FF\s\u0750-\u077F\uFB50-\uFDFF\uFE70-\uFEFF]',
            '',
            name,
        )
        name = ' '.join(name.split())
        return name.strip() or "untitled"

    # ------------------------------------------------------------------ #
    def _build_ydl_opts(self, flag: dict, extra: dict = None):
        opts = {
            'quiet': True,
            'noplaylist': True,
            'socket_timeout': 60,
            'geo_bypass': True,
            'nocheckcertificate': True,
            'no_warnings': True,
        }
        if flag and flag.get('op') and os.path.exists(COOKIES_FILE):
            opts['cookies'] = COOKIES_FILE
        if extra:
            opts.update(extra)
        return opts

    # ------------------------------------------------------------------ #
    @staticmethod
    def _quality_label(fmt_dict):
        """
        الحصول على تسمية الجودة من الفيديو.
        يُرجع height (int) إن وُجد، وإلا يرجع format_note (str) كـ fallback
        لدعم صيغ مثل HD/SD من فيسبوك.
        """
        h = fmt_dict.get('height') or 0
        if h:
            return h
        note = (fmt_dict.get('format_note') or '').strip()
        if note:
            return note  # مثلاً "HD", "SD", "hd", "sd"
        return 0

    # ------------------------------------------------------------------ #
    def _fetch_innertube(self, video_id: str) -> dict | None:
        """
        استخراج معلومات الفيديو عبر InnerTube API مباشرةً.
        نُجرّب عدة عملاء بالترتيب لتفادي مشاكل Android client الذي
        أصبح يطلب PoToken في كثير من الحالات (HTTP 400):
          1) IOS         — أكثرها استقراراً حالياً، لا يحتاج PoToken.
          2) ANDROID     — قد يفشل بـ 400 لكن يعطي أحجام دقيقة عندما يعمل.
          3) TVHTML5     — fallback إضافي يعمل لمعظم الفيديوهات العامة.
        يُرجع None عند فشل الكل للرجوع إلى yt-dlp.
        """
        url = "https://www.youtube.com/youtubei/v1/player"
        # نُعرّف 3 عملاء بالترتيب: iOS أولاً (الأكثر ثباتاً)
        clients = [
            {
                "name": "IOS",
                "context_client": {
                    "clientName": "IOS",
                    "clientVersion": "19.45.4",
                    "deviceMake": "Apple",
                    "deviceModel": "iPhone16,2",
                    "osName": "iPhone",
                    "osVersion": "17.5.1.21F90",
                    "hl": "en",
                    "gl": "US",
                },
                "headers": {
                    "User-Agent": "com.google.ios.youtube/19.45.4 (iPhone16,2; U; CPU iOS 17_5_1 like Mac OS X)",
                    "X-YouTube-Client-Name": "5",
                    "X-YouTube-Client-Version": "19.45.4",
                },
            },
            {
                "name": "ANDROID",
                "context_client": {
                    "clientName": "ANDROID",
                    "clientVersion": "19.44.38",
                    "androidSdkVersion": 34,
                    "hl": "en",
                    "gl": "US",
                },
                "headers": {
                    "User-Agent": "com.google.android.youtube/19.44.38 (Linux; U; Android 14) gzip",
                    "X-YouTube-Client-Name": "3",
                    "X-YouTube-Client-Version": "19.44.38",
                },
            },
            {
                "name": "TVHTML5",
                "context_client": {
                    "clientName": "TVHTML5_SIMPLY_EMBEDDED_PLAYER",
                    "clientVersion": "2.0",
                    "hl": "en",
                    "gl": "US",
                },
                "headers": {
                    "User-Agent": "Mozilla/5.0 (PlayStation; PlayStation 4/12.00) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15",
                    "X-YouTube-Client-Name": "85",
                    "X-YouTube-Client-Version": "2.0",
                },
            },
        ]

        for client in clients:
            try:
                payload = {
                    "videoId": video_id,
                    "context": {"client": client["context_client"]},
                    # نُعطّل التحقق من سن المستخدم لتجنّب الرفض على بعض الفيديوهات
                    "racyCheckOk": True,
                    "contentCheckOk": True,
                }
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "*/*",
                    "Accept-Language": "en-US,en;q=0.9",
                    "Origin": "https://www.youtube.com",
                }
                headers.update(client["headers"])

                resp = requests.post(url, json=payload, headers=headers, timeout=10)
                if resp.status_code != 200:
                    print(f"[InnerTube/{client['name']}] HTTP {resp.status_code}")
                    continue

                data = resp.json()

                # تحقق من حالة التشغيل
                play_status = data.get("playabilityStatus", {}).get("status")
                if play_status not in (None, "OK"):
                    print(f"[InnerTube/{client['name']}] playabilityStatus: {play_status}")
                    continue

                # استخرج العنوان والمدة والثامب
                details = data.get("videoDetails", {})
                title = details.get("title", "untitled") or "untitled"
                duration = int(details.get("lengthSeconds", 0) or 0)
                thumbs = details.get("thumbnail", {}).get("thumbnails", [])
                thumbnail = thumbs[-1]["url"] if thumbs else ""

                # استخرج الفورمات من streamingData
                streaming = data.get("streamingData", {})
                formats_raw = streaming.get("adaptiveFormats", [])

                keys = [144, 240, 360, 480, 720, 1080]
                keys_str = ['144', '240', '360', '480', '720', '1080']
                audio_qualities = {}
                video_qualities = {}

                for fmt in formats_raw:
                    mime = fmt.get("mimeType", "")
                    content_length = fmt.get("contentLength")
                    if content_length is None:
                        bitrate = fmt.get("bitrate", 0) or 0
                        content_length = int(bitrate * duration / 8) if duration else 0
                    size_mb = round(int(content_length) / (1024 * 1024), 2)
                    fmt_id = str(fmt.get("itag", ""))

                    has_video = "video/" in mime
                    has_audio = "audio/" in mime

                    if has_audio and not has_video:
                        audio_qualities[fmt_id] = size_mb
                    elif has_video and not has_audio:
                        height = fmt.get("height", 0) or 0
                        height_str = str(height)
                        if height in keys or height_str in keys_str:
                            video_qualities.setdefault(height_str, []).append(
                                [fmt_id, size_mb]
                            )

                if not audio_qualities:
                    print(f"[InnerTube/{client['name']}] بيانات صوت ناقصة، نجرّب العميل التالي.")
                    continue

                print(f"[InnerTube/{client['name']}] نجح الاستخراج ✓")
                return {
                    "title": title,
                    "duration": duration,
                    "thumbnail": thumbnail,
                    "audio_qualities": audio_qualities,
                    "video_qualities": video_qualities,
                }
            except Exception as e:
                print(f"[InnerTube/{client['name']}] فشل: {e}")
                continue

        # كل العملاء فشلوا
        return None

    # ------------------------------------------------------------------ #
    def information(self, url, flag: dict):
        """استخراج معلومات فيديو يوتيوب وحفظ كاش JSON."""
        print("Start information fun : ")
        self.bool_dict_info = False
        self.youtube_audio_qualities = {}
        self.youtube_video_qualities = {}
        self.info_url = {}

        keys = [144, 240, 360, 480, 720, 1080]
        keys_str = ['144', '240', '360', '480', '720', '1080']

        url = url.split("&")[0]

        if "youtu" not in url:
            return None

        self.name_image = url[-11:]
        name_json = self.name_image
        print(f"start analysis : {name_json}")

        cache_path = os.path.join(CACHE_INFO_DIR, f"{name_json}.json")
        cache_loaded = False
        if os.path.exists(cache_path):
            try:
                with open(cache_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                # تحقق من وجود كل المفاتيح المطلوبة قبل استخدامها
                if (
                    isinstance(data, dict)
                    and "youtube_audio_qualities" in data
                    and "youtube_video_qualities" in data
                    and "info_url" in data
                    and data["youtube_audio_qualities"]
                ):
                    self.youtube_audio_qualities = dict(data["youtube_audio_qualities"])
                    self.youtube_video_qualities = dict(data["youtube_video_qualities"])
                    self.info_url = dict(data["info_url"])
                    self.info_url["title"] = self.clean_filename(
                        self.info_url.get("title", "untitled")
                    )
                    cache_loaded = True
                else:
                    print(f"[info] كاش قديم/ناقص في {cache_path}، سيُعاد الاستخراج.")
            except (json.JSONDecodeError, KeyError, TypeError) as ce:
                print(f"[info] كاش تالف ({ce})، سيُعاد الاستخراج.")
                # احذف الكاش التالف
                try:
                    os.remove(cache_path)
                except Exception:
                    pass

        if not cache_loaded:
            # --- محاولة InnerTube أولاً (أسرع بكثير) ---
            innertube_data = self._fetch_innertube(self.name_image)

            if innertube_data:
                self.info_url = {
                    "title": self.clean_filename(innertube_data["title"]),
                    "thumbnail": innertube_data["thumbnail"],
                    "time": innertube_data["duration"],
                }
                self.youtube_audio_qualities = innertube_data["audio_qualities"]
                self.youtube_video_qualities = innertube_data["video_qualities"]
            else:
                # --- Fallback إلى yt-dlp ---
                print("[InnerTube] فشل، الرجوع إلى yt-dlp...")
                ydl_opts = self._build_ydl_opts(flag)
                with yt_dlp.YoutubeDL(ydl_opts) as yt:
                    info = yt.extract_info(url, download=False)

                self.info_url = {
                    "title": self.clean_filename(info.get('title', 'untitled')),
                    "thumbnail": info.get('thumbnail', ''),
                    "time": info.get('duration', 0) or 0,
                }

                for i in info.get('formats', []) or []:
                    filesize = i.get('filesize')
                    if filesize is not None:
                        filesize = round(filesize / (1024 * 1024), 2)
                        if i.get('vcodec') == 'none' and i.get('acodec') != 'none':
                            self.youtube_audio_qualities[i.get('format_id')] = filesize
                        if (
                            i.get("format_note")
                            and i.get('acodec') == 'none'
                            and (
                                i.get('height') in keys
                                or i.get('format_note')[:-1] in keys_str
                            )
                        ):
                            self.youtube_video_qualities.setdefault(
                                str(i.get('format_note')[:-1]), []
                            ).append([i.get('format_id'), filesize])

            if self.youtube_audio_qualities and self.youtube_video_qualities:
                with open(cache_path, "w", encoding="utf-8") as f:
                    json.dump(
                        {
                            "youtube_audio_qualities": self.youtube_audio_qualities,
                            "youtube_video_qualities": self.youtube_video_qualities,
                            "info_url": self.info_url,
                        },
                        f,
                        indent=4,
                        ensure_ascii=False,
                    )

        return self.youtube_audio_qualities, self.youtube_video_qualities, self.info_url

    # ------------------------------------------------------------------ #
    @staticmethod
    def _has_codec(codec_val):
        """
        التحقق من وجود codec صالح.
        يعالج الحالات: None, '', 'none', 'null'
        """
        if not codec_val:
            return False
        return str(codec_val).strip().lower() not in ('', 'none', 'null')

    def information_force(self, url, flag: dict):
        """
        استخراج معلومات أي رابط (يوتيوب/فيسبوك/ساوندكلاود/...).
        لا يفرض شرط يوتيوب — يعتمد على ما يدعمه yt-dlp.
        لو فشل yt-dlp تماماً في فهم الرابط (رابط "غريب" غير مدعوم)، أو
        فهمه لكن لم يُرجع أي تنسيقات، نفحص صفحة الويب يدوياً بحثاً عن أي
        روابط فيديو/صوت مباشرة (mp4, webm, m3u8, mp3, m4a ...) كحل بديل.
        """
        print("start information force : ")
        try:
            ydl_opts = self._build_ydl_opts(flag)
            with yt_dlp.YoutubeDL(ydl_opts) as yt:
                info = yt.extract_info(url, download=False) or {}
        except Exception as e:
            print(f"[force] فشل yt-dlp في فهم الرابط ({e})، سيتم البحث اليدوي في الصفحة.")
            info = {}

        title_raw = info.get('title', 'untitled') or 'untitled'
        # تنظيف العنوان عبر clean_filename لضمان سلامة اسم الملف
        title = self.clean_filename(title_raw.split('|')[-1].strip())
        duration = info.get('duration', 0) or 0
        thumb = info.get('thumbnail', '') or ''
        info_url = [title, duration, thumb]

        audio = {}
        video = {}
        video_audio = {}
        ac = vc = v_ac = 0

        for i in info.get('formats') or []:
            size_temp = 0
            if i.get('filesize'):
                size_temp = i.get('filesize') / 1024
            elif i.get('filesize_approx'):
                size_temp = i.get('filesize_approx') / 1024
            elif i.get('http_chunk_size'):
                size_temp = i.get('http_chunk_size') / 1024
            elif i.get('tbr'):
                size_temp = (i.get('tbr') * (duration or 0)) / 8
            else:
                a = i.get('abr') or 0
                v = i.get('vbr') or 0
                size_temp = ((a + v) * (duration or 0)) / 8

            size = round(size_temp / 1024, 2)
            vcodec = i.get('vcodec')
            acodec = i.get('acodec')
            has_v = self._has_codec(vcodec)
            has_a = self._has_codec(acodec)

            if not has_v and not has_a:
                h = i.get('height') or 0
                a_br = i.get('abr') or 0
                if h:
                    has_v = True
                if a_br:
                    has_a = True
                if h and i.get('tbr'):
                    has_a = True

            if has_v and has_a:
                video_audio[v_ac] = [self._quality_label(i), i.get('format_id'), size]
                v_ac += 1
            elif has_v and not has_a:
                video[vc] = [self._quality_label(i), i.get('format_id'), size]
                vc += 1
            elif not has_v and has_a:
                audio[ac] = [i.get('abr') or 0, i.get('format_id'), size]
                ac += 1
            else:
                # صيغة لا يحدد لها yt-dlp أكواد صوت/فيديو صريحة ولا height/abr
                # (شائع في بعض المواقع غير يوتيوب)؛ كانت تُهمَل بالكامل سابقاً
                # رغم أنها رابط ميديا فعلي صالح للتحميل. نستبعد فقط لوحات
                # المعاينة (storyboard/mhtml) ونعامل الباقي كملف مدمج.
                fmt_ext = (i.get('ext') or '').lower()
                protocol = (i.get('protocol') or '').lower()
                note_l = (i.get('format_note') or '').lower()
                is_storyboard = (
                    fmt_ext == 'mhtml' or 'storyboard' in note_l or 'mhtml' in protocol
                )
                has_media_url = bool(i.get('url') or i.get('manifest_url'))
                if not is_storyboard and has_media_url and i.get('format_id'):
                    label = self._quality_label(i) or i.get('format_note') or fmt_ext.upper() or 'ملف'
                    video_audio[v_ac] = [label, i.get('format_id'), size]
                    v_ac += 1

        # === فيسبوك: ضمان وجود فورماتين أساسيين sd و hd دائماً ===
        if _is_facebook_url(url):
            # في فيسبوك يدعم yt-dlp محددات جاهزة باسم sd و hd؛
            # نضيفهما دائماً لو لم يكونا موجودين كـ format_id حتى تظهر في التبويب المدمج.
            existing_ids = {str(v[1]).strip().lower() for v in video_audio.values()}

            if 'sd' not in existing_ids:
                video_audio[v_ac] = ['SD', 'sd', 0]
                v_ac += 1

            if 'hd' not in existing_ids:
                video_audio[v_ac] = ['HD', 'hd', 0]
                v_ac += 1

        # === رابط "غريب" لا يفهمه yt-dlp أو لم يُرجع أي تنسيقات: فحص يدوي للصفحة === #
        if not audio and not video and not video_audio:
            print("[force] لا توجد تنسيقات من yt-dlp — جاري فحص الصفحة يدوياً عن روابط ميديا.")
            g_audio, g_video_audio, g_info = _scan_page_for_media(url)
            if g_audio or g_video_audio:
                audio, video_audio = g_audio, g_video_audio
                if not title or title == "untitled":
                    title = self.clean_filename(g_info[0])
                    info_url = [title, duration, thumb]

        return audio, video, video_audio, info_url
    # ------------------------------------------------------------------ #
    def sort_video_qualities(self, url, flag: dict):
        """ترتيب جودات الصوت والفيديو حسب الحجم."""
        result = self.information(url, flag)
        if result is None:
            return {}, {}, ["", "", "00:00:00"]
        audio_qualities, video_qualities, info = result

        sorted_audio_asc = dict(sorted(audio_qualities.items(), key=lambda item: item[1]))

        for quality, formats_list in video_qualities.items():
            video_qualities[quality] = sorted(formats_list, key=lambda x: x[1])

        t = info.get('time', 0) or 0
        time_str = f"{t // 3600:02}:{(t % 3600) // 60:02}:{t % 60:02}"
        info_video = [
            self.clean_filename(info.get('title', '')),
            info.get('thumbnail', ''),
            time_str,
        ]
        return sorted_audio_asc, video_qualities, info_video

    # ------------------------------------------------------------------ #
    def picture(self, image_url, local_path=CACHE_IMAGES_DIR):
        """
        تحميل وتجهيز الصورة المصغرة وإرجاعها كـ QPixmap (بدل CTkImage).
        تطبّق قناعاً دائرياً (rounded corners).
        """
        if not image_url:
            return QPixmap()

        url_hash = hashlib.md5(image_url.encode('utf-8')).hexdigest()
        # نحفظ كـ PNG لدعم الشفافية بدل JPEG
        unique_name = f"image_{url_hash}.png"
        local_image_path = os.path.join(local_path, unique_name)

        if not os.path.exists(local_path):
            os.makedirs(local_path, exist_ok=True)

        try:
            if os.path.exists(local_image_path):
                img = Image.open(local_image_path).convert("RGBA").resize((247, 117))
            else:
                response = requests.get(image_url, timeout=30)
                img = Image.open(BytesIO(response.content)).convert("RGBA").resize((247, 117))
                # احفظ كـ PNG لتجنب خطأ "cannot write mode RGBA as JPEG"
                img.save(local_image_path, format="PNG")
        except Exception as e:
            print(f"Error loading thumbnail: {e}")
            return QPixmap()

        # قناع زوايا دائرية
        mask = Image.new("L", (247, 117), 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle((0, 0, 247, 117), radius=15, fill=255)
        img.putalpha(mask)

        # تحويل PIL → QPixmap
        data = img.tobytes("raw", "RGBA")
        qimg = QImage(data, img.width, img.height, QImage.Format.Format_RGBA8888)
        pix = QPixmap.fromImage(qimg)
        return pix

    # ------------------------------------------------------------------ #
    def fun_for_all(self, url, flag: dict):
        """معالجة شاملة: إرجاع id/sizes للجودات المنخفضة والعالية + معلومات الفيديو."""
        audio, video, info_process = self.sort_video_qualities(url, flag)

        all_low_id, all_low_size = [], []
        all_heigh_id, all_heigh_size = [], []

        if not audio:
            # لا توجد بيانات؛ نُرجع قوائم فارغة
            return [], [], [], [], info_process

        audio_list = list(dict(audio).items())
        all_low_id.extend([audio_list[0][0], audio_list[-1][0]])
        all_low_size.extend([audio_list[0][1], audio_list[-1][1]])
        all_heigh_id.extend([audio_list[0][0], audio_list[-1][0]])
        all_heigh_size.extend([audio_list[0][1], audio_list[-1][1]])

        keys = list(video.keys())
        keys_str = ['144', '240', '360', '480', '720', '1080']

        for quality in keys_str:
            if quality in keys:
                all_low_id.append(video[quality][0][0])
                all_low_size.append(video[quality][0][1])
                all_heigh_id.append(video[quality][-1][0])
                all_heigh_size.append(video[quality][-1][1])
            else:
                all_low_id.append("")
                all_low_size.append("")
                all_heigh_id.append("")
                all_heigh_size.append("")

        return all_low_id, all_low_size, all_heigh_id, all_heigh_size, info_process

    # ------------------------------------------------------------------ #
    def downloading(self, url, id_url, path, flag: dict, callbacks: dict,
                    pause_event=None, cancel_event=None):
        """
        تنزيل عبر yt-dlp.
        - flag: قاموس يحتوي على 'op' (كوكيز) و 'subtitle' (ترجمة).
        - callbacks: dict {'progress': fn(percent), 'status_change': fn(str)}
        - pause_event / cancel_event: threading.Event من DownloadManager.
          استخدام Events بدل flag["resume"] القديم (الذي كان مربكاً).
          ملاحظة: yt-dlp لا يدعم Pause حقيقياً، فالـ Pause = إيقاف العملية مع
          الحفاظ على ملفات .part بحيث يستأنف عند الضغط على Resume بفضل
          continue_dl=True.
        """
        path = re.sub(r'[#]', '', path)
        progress = callbacks.get('progress', lambda p: None)
        status_change = callbacks.get('status_change', lambda s: None)
        speed_cb = callbacks.get('speed', lambda s: None)
        size_cb = callbacks.get('size', lambda downloaded, total, stream_type='': None)

        # --- تحميل مباشر لرابط ميديا تم اكتشافه يدوياً من صفحة "غريبة" --- #
        # (رابط لا يفهمه yt-dlp؛ راجع _scan_page_for_media / information_force)
        if isinstance(id_url, str) and id_url.startswith("direct:"):
            direct_url = id_url[len("direct:"):]
            return self._download_direct(direct_url, path, callbacks, pause_event, cancel_event)

        def progress_hook(d):
            # إيقاف فوري عند طلب Cancel أو Pause
            if cancel_event is not None and cancel_event.is_set():
                raise StopDownload("Download cancelled by user.")
            if pause_event is not None and pause_event.is_set():
                raise StopDownload("Download paused by user.")

            if d.get('status') == 'downloading':
                total = d.get('total_bytes') or d.get('total_bytes_estimate') or 1
                downloaded = d.get('downloaded_bytes', 0) or 0
                percent = downloaded / total * 100 if total else 0
                progress(percent)

                info = d.get('info_dict', {}) or {}
                is_audio_only = bool(
                    info.get("acodec") and info.get("acodec") != "none"
                    and (not info.get("vcodec") or info.get("vcodec") == "none")
                )
                is_video = bool(info.get("vcodec") and info.get("vcodec") != "none")
                if is_audio_only:
                    stream_type = "الصوت"
                elif is_video:
                    stream_type = "الفيديو"
                else:
                    stream_type = "الملف"

                try:
                    size_cb(float(downloaded), float(total or 0), stream_type)
                except Exception:
                    pass

                spd = d.get('speed') or 0
                if spd:
                    spd_str = self._fmt_speed(spd)
                    speed_cb(spd_str)

                if is_audio_only:
                    status_change("تحميل الصوت")
                elif is_video:
                    status_change("تحميل الفيديو")
            elif d.get('status') == 'finished':
                status_change("جاري الدمج...")

        options = {
            'format': id_url,
            'ffmpeg_location': FFMPEG,
            'outtmpl': path,
            'continue_dl': True,
            'quiet': True,
            'retries': 15,
            'fragment_retries': 15,
            'file_access_retries': 5,
            'concurrent_fragment_downloads': 3,
            'progress_hooks': [progress_hook],
            'ignoreerrors': True,
            'no_warnings': True,
            'socket_timeout': 60,
            'age_limit': 0,
            'geo_bypass': True,
            'geo_bypass_country': 'US',
            'referer': 'https://www.youtube.com/',
            'merge_output_format': 'mp4',
        }

        if flag.get('op') and os.path.exists(COOKIES_FILE):
            options['cookies'] = COOKIES_FILE
            options['http_headers'] = {'User-Agent': 'Mozilla/5.0'}

        try:
            status_change("بدء التحميل...")
            with yt_dlp.YoutubeDL(options) as file:
                # مهم: نلتقط كود الإرجاع. مع ignoreerrors=True لا يرمي yt-dlp
                # استثناءً عند فشل جزء من التحميل (مثلاً فشل تحميل مسار الفيديو
                # بينما نجح الصوت) — لكنه يُرجع كوداً غير صفري في هذه الحالة،
                # وكان البرنامج سابقاً يتجاهله تماماً ويعتبر التحميل ناجحاً.
                retcode = file.download([url])

            # إذا تم إلغاء التحميل أثناء العملية ووصل الكود إلى هنا (نادر)
            if cancel_event is not None and cancel_event.is_set():
                status_change("تم إلغاء التحميل")
                return False
            if pause_event is not None and pause_event.is_set():
                status_change("متوقف مؤقتاً")
                return False

            if retcode:
                status_change("فشل التحميل (تعذّر إكمال كل الأجزاء)")
                print(f"[downloading] yt-dlp أرجع كود خطأ: {retcode}")
                return False

            # تحقق فعلي من وجود الملف الناتج وأن حجمه ليس صفراً، بدل افتراض
            # النجاح لمجرد عدم حدوث استثناء.
            final_file = _resolve_media_file(path)
            if not os.path.exists(final_file) or os.path.getsize(final_file) <= 0:
                status_change("لم يكتمل التحميل: الملف غير موجود")
                print(f"[downloading] الملف الناتج غير موجود أو فارغ: {final_file}")
                return False

            # للتنسيقات المدمجة (صوت + فيديو، مثل "140+137") تحقق عبر ffmpeg من
            # أن الملف النهائي يحتوي فعلاً على مساري صوت وفيديو معاً، لمعالجة
            # حالة "قال اكتمل التحميل لكن الصوت فقط تم تحميله دون الفيديو" (أو
            # العكس) رغم عدم حدوث استثناء وعدم وجود كود خطأ.
            if "+" in str(id_url):
                has_v, has_a = self._probe_streams(final_file)
                if not has_v or not has_a:
                    missing = "الفيديو" if not has_v else "الصوت"
                    status_change(f"التحميل غير مكتمل: بدون {missing}")
                    print(f"[downloading] فشل التحقق من المسارات في {final_file}: "
                          f"فيديو={has_v} صوت={has_a}")
                    return False

            status_change("تم التحميل بنجاح")

            # تحميل الترجمة إن طُلب
            if flag.get('subtitle'):
                try:
                    status_change("جاري تحميل الترجمة...")
                    download_and_fix_subtitle(url, path, flag.get("subtitle_lang", "ar"))
                    status_change("تم تحميل الترجمة + الفيديو")
                except Exception as se:
                    print(f"Subtitle error: {se}")
                    status_change("تم التحميل (تعذّر جلب الترجمة)")

            return True
        except StopDownload as sd:
            print(f"Download stopped: {sd}")
            if cancel_event is not None and cancel_event.is_set():
                status_change("تم إلغاء التحميل")
            else:
                status_change("متوقف مؤقتاً")
            return False
        except Exception as e:
            status_change("حدث خطأ")
            print(f"Error during download: {str(e)}")
            return False

    @staticmethod
    def _fmt_speed(speed_bytes):
        units = ['B/s', 'KB/s', 'MB/s', 'GB/s']
        s = float(speed_bytes)
        i = 0
        while s >= 1024 and i < len(units) - 1:
            s /= 1024
            i += 1
        return f"{s:.1f} {units[i]}"

    # ------------------------------------------------------------------ #
    @staticmethod
    def _probe_streams(filepath: str):
        """
        يتحقق عبر ffmpeg (بدون تحويل، مجرد قراءة معلومات) من وجود مسار فيديو
        و/أو مسار صوت داخل الملف الناتج. يُستخدم للتأكد من نجاح الدمج الفعلي
        بعد تحميل مدمج (صوت+فيديو)، بدل الاكتفاء بعدم وجود استثناء.
        يُرجع (has_video, has_audio).
        """
        has_v = has_a = False
        try:
            proc = subprocess.run(
                [FFMPEG, "-hide_banner", "-i", filepath],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=25,
                creationflags=_CREATE_NO_WINDOW if sys.platform.startswith("win") else 0,
            )
            out = (proc.stderr or b"").decode("utf-8", errors="ignore")
            for line in out.splitlines():
                l = line.strip()
                if l.startswith("Stream #") and ": Video:" in l:
                    has_v = True
                elif l.startswith("Stream #") and ": Audio:" in l:
                    has_a = True
        except Exception as e:
            print(f"[probe_streams] تعذّر فحص الملف عبر ffmpeg: {e}")
            # تعذّر الفحص لا يعني بالضرورة فشل التحميل؛ لا نمنع النجاح هنا
            # (سيتم الاعتماد على الفحوصات الأخرى: كود الإرجاع ووجود الملف).
            return True, True
        return has_v, has_a

    # ------------------------------------------------------------------ #
    def _download_direct(self, direct_url, path, callbacks, pause_event=None, cancel_event=None):
        """
        تحميل مباشر (بدون yt-dlp) لملف ميديا تم اكتشافه يدوياً من صفحة ويب
        "غريبة" لا يفهمها yt-dlp. يبثّ التقدّم/السرعة/الحجم عبر نفس الـ
        callbacks المستخدمة في التحميل العادي، ويتحقق من نجاح الحفظ فعلياً.
        """
        progress = callbacks.get('progress', lambda p: None)
        status_change = callbacks.get('status_change', lambda s: None)
        speed_cb = callbacks.get('speed', lambda s: None)
        size_cb = callbacks.get('size', lambda downloaded, total, stream_type='': None)

        headers = {"User-Agent": _GENERIC_UA, "Accept": "*/*"}
        tmp_path = path + ".part"
        try:
            directory = os.path.dirname(path) or "."
            os.makedirs(directory, exist_ok=True)

            status_change("بدء التحميل...")
            with requests.get(direct_url, headers=headers, stream=True, timeout=30) as r:
                r.raise_for_status()
                total = int(r.headers.get("Content-Length") or 0)
                downloaded = 0
                t0 = time.time()
                last_emit = t0
                with open(tmp_path, "wb") as f:
                    for chunk in r.iter_content(chunk_size=256 * 1024):
                        if cancel_event is not None and cancel_event.is_set():
                            status_change("تم إلغاء التحميل")
                            return False
                        if pause_event is not None and pause_event.is_set():
                            status_change("متوقف مؤقتاً")
                            return False
                        if not chunk:
                            continue
                        f.write(chunk)
                        downloaded += len(chunk)
                        now = time.time()
                        if total:
                            try:
                                progress(downloaded / total * 100)
                            except Exception:
                                pass
                        if now - last_emit >= 0.2:
                            elapsed = max(now - t0, 0.001)
                            try:
                                speed_cb(self._fmt_speed(downloaded / elapsed))
                                size_cb(float(downloaded), float(total or 0), "الملف")
                            except Exception:
                                pass
                            status_change("جاري التحميل...")
                            last_emit = now

            # تحقق فعلي: هل الملف موجود وحجمه أكبر من صفر؟ (نفس مبدأ التحقق
            # المستخدم في مسار yt-dlp، بدل افتراض النجاح لمجرد انتهاء الحلقة).
            if not os.path.exists(tmp_path) or os.path.getsize(tmp_path) <= 0:
                status_change("فشل التحميل: الملف فارغ")
                try:
                    if os.path.exists(tmp_path):
                        os.remove(tmp_path)
                except Exception:
                    pass
                return False

            os.replace(tmp_path, path)
            status_change("تم التحميل بنجاح")
            return True
        except Exception as e:
            status_change("حدث خطأ أثناء التحميل المباشر")
            print(f"[download_direct] خطأ: {e}")
            try:
                if os.path.exists(tmp_path):
                    os.remove(tmp_path)
            except Exception:
                pass
            return False

    # ------------------------------------------------------------------ #
    def choice_path_back(self, btn, path):
        """إدارة قراءة/كتابة path.json. لا تتغيّر آلية المسارات."""
        data = {}
        try:
            with open(PATHS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            d = default_downloads_dir()
            data["path_video"] = d
            data["path_audio"] = d
            data["path_list"] = d

        if btn == "self.path_video_btn":
            data["path_video"] = f"{path}"
        elif btn == "self.path_audio_btn":
            data["path_audio"] = f"{path}"
        elif btn == "self.path_list_btn":
            data["path_list"] = f"{path}"

        try:
            _atomic_write_text(PATHS_FILE, json.dumps(data, ensure_ascii=False, indent=4))
        except Exception as e:
            print(f"[paths] خطأ حفظ مسارات الحفظ: {e}")

        return data

def load_paths():
    """قراءة path.json أو إنشاؤه بالقيم الافتراضية إن لم يوجد."""
    d = default_downloads_dir()
    default = {"path_video": d, "path_audio": d, "path_list": d}
    try:
        if not os.path.exists(PATHS_FILE):
            _atomic_write_text(PATHS_FILE, json.dumps(default, ensure_ascii=False, indent=4))
            return default
        with open(PATHS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise ValueError("ملف مسارات غير صالح")
        for k, v in default.items():
            data.setdefault(k, v)
        return data
    except Exception as e:
        print(f"[paths] ملف مسارات تالف أو غير مقروء، إعادة الإنشاء بالقيم الافتراضية: {e}")
        try:
            _atomic_write_text(PATHS_FILE, json.dumps(default, ensure_ascii=False, indent=4))
        except Exception:
            pass
        return default


MAX_HISTORY = 500  # حد أقصى للسجل


# ----------------------------- DownloadTask --------------------------------- #
_task_id_counter = itertools.count(1)


@dataclass
class DownloadTask:
    """مهمة تحميل واحدة."""
    url: str
    format_id: str  # مثل "22" أو "140+137"
    output_path: str  # المسار الكامل (بدون امتداد للفيديو، مع .mp3 للصوت)
    flag: dict = field(default_factory=lambda: {"op": False, "subtitle": False})
    task_id: int = field(default_factory=lambda: next(_task_id_counter))
    display_name: str = ""  # اسم يُعرض في البطاقة
    thumbnail_url: str = ""  # رابط الصورة المصغرة للتحميل (إن وُجد)

    def __post_init__(self):
        if not self.display_name:
            self.display_name = os.path.basename(self.output_path) or self.url


# ----------------------------- Status Constants ----------------------------- #
STATUS_PENDING = "pending"      # في الانتظار
STATUS_RUNNING = "running"      # قيد التحميل
STATUS_PAUSED = "paused"        # متوقف مؤقتاً
STATUS_DONE = "done"            # تم
STATUS_ERROR = "error"          # خطأ
STATUS_CANCELLED = "cancelled"  # ألغي


# ----------------------------- DownloadWorker ------------------------------- #
class DownloadWorker(QObject):
    """يعمل داخل QThread؛ يبثّ التقدّم والحالة عبر signals."""
    progress = pyqtSignal(int, float)          # task_id, percent
    status = pyqtSignal(int, str)              # task_id, نص الحالة المعروض
    speed = pyqtSignal(int, str)               # task_id, نص السرعة
    size = pyqtSignal(int, float, float, str)  # task_id, downloaded_MB, total_MB, نوع الستريم
    finished = pyqtSignal(int, bool)           # task_id, success

    def __init__(self, task: DownloadTask):
        super().__init__()
        self.task = task
        self.pause_event = threading.Event()
        self.cancel_event = threading.Event()
        self._backend = YouTubeDownloader()

    def request_pause(self):
        self.pause_event.set()

    def request_cancel(self):
        self.cancel_event.set()

    def run(self):
        """نقطة الدخول التي يستدعيها QThread.started."""
        def on_progress(p):
            self.progress.emit(self.task.task_id, float(p))

        def on_status(s):
            self.status.emit(self.task.task_id, str(s))

        def on_speed(s):
            self.speed.emit(self.task.task_id, str(s))

        def on_size(downloaded_bytes, total_bytes, stream_type=""):
            try:
                d_mb = downloaded_bytes / (1024 * 1024)
                t_mb = total_bytes / (1024 * 1024) if total_bytes else 0.0
                self.size.emit(self.task.task_id, float(d_mb), float(t_mb), str(stream_type or ""))
            except Exception:
                pass

        callbacks = {
            'progress': on_progress,
            'status_change': on_status,
            'speed': on_speed,
            'size': on_size,
        }

        try:
            success = self._backend.downloading(
                self.task.url,
                self.task.format_id,
                self.task.output_path,
                self.task.flag,
                callbacks,
                pause_event=self.pause_event,
                cancel_event=self.cancel_event,
            )
        except Exception as e:
            print(f"[worker] خطأ غير متوقع: {e}")
            success = False

        self.finished.emit(self.task.task_id, bool(success))


# ----------------------------- DownloadManager ------------------------------ #
class DownloadManager(QObject):
    """Singleton — مدير التحميلات المركزي."""
    _instance: Optional["DownloadManager"] = None

    # Signals تُرسل إلى downloads_tab وغيره
    task_added = pyqtSignal(object)             # DownloadTask
    task_progress = pyqtSignal(int, float)      # task_id, percent
    task_status = pyqtSignal(int, str)          # task_id, str
    task_speed = pyqtSignal(int, str)           # task_id, str
    task_size = pyqtSignal(int, float, float, str)  # task_id, downloaded_MB, total_MB, نوع الستريم
    task_finished = pyqtSignal(int, bool)       # task_id, success
    task_state_changed = pyqtSignal(int, str)   # task_id, STATUS_*
    max_parallel_changed = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        if DownloadManager._instance is not None:
            raise RuntimeError("استخدم DownloadManager.instance()")
        self._max_parallel = 3
        self._tasks: Dict[int, DownloadTask] = {}
        self._states: Dict[int, str] = {}
        self._workers: Dict[int, DownloadWorker] = {}
        self._threads: Dict[int, QThread] = {}
        self._pending: List[int] = []
        self._resume_after_cleanup = set()
        self._shutting_down = False
        self._mutex = QMutex()
        # السجل الكامل للتحميلات (يُحفظ على القرص)
        self._history: List[dict] = []
        self._load_history()

    @classmethod
    def instance(cls) -> "DownloadManager":
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    # ------------------------- التحكم في التوازي --------------------------- #
    def set_max_parallel(self, n: int):
        n = max(1, min(10, int(n)))
        self._max_parallel = n
        self.max_parallel_changed.emit(n)
        self._try_start_pending()

    def max_parallel(self) -> int:
        return self._max_parallel

    # ------------------------- إضافة/إدارة المهام -------------------------- #
    def add_task(self, task: DownloadTask):
        """إضافة مهمة جديدة، تبدأ فوراً إن توفّر slot وإلا تنتظر."""
        if self._shutting_down:
            return
        with QMutexLocker(self._mutex):
            self._tasks[task.task_id] = task
            self._states[task.task_id] = STATUS_PENDING
            self._pending.append(task.task_id)
        # سجّل المهمة فوراً في السجل (بحالة pending)
        self.record_history(task, STATUS_PENDING)
        self.task_added.emit(task)
        self.task_state_changed.emit(task.task_id, STATUS_PENDING)
        self._try_start_pending()

    def _active_count(self) -> int:
        return sum(1 for s in self._states.values() if s == STATUS_RUNNING)

    def _try_start_pending(self):
        # يبدأ مهام من القائمة قدر ما يسمح max_parallel
        while True:
            with QMutexLocker(self._mutex):
                if not self._pending:
                    return
                if self._active_count() >= self._max_parallel:
                    return
                # خذ أول مهمة من الانتظار
                task_id = self._pending.pop(0)
                task = self._tasks.get(task_id)
                if task is None:
                    continue
                # لو Worker قديم لنفس المهمة لم ينتهِ بعد (Pause/Resume سريع)، انتظر تنظيفه.
                if task_id in self._workers:
                    self._resume_after_cleanup.add(task_id)
                    continue
                self._states[task_id] = STATUS_RUNNING
            self._start_worker(task)
            self.task_state_changed.emit(task.task_id, STATUS_RUNNING)

    def _start_worker(self, task: DownloadTask):
        thread = QThread()
        worker = DownloadWorker(task)
        worker.moveToThread(thread)

        # Signals → forward
        worker.progress.connect(self.task_progress)
        worker.status.connect(self.task_status)
        worker.speed.connect(self.task_speed)
        worker.size.connect(self.task_size)
        worker.finished.connect(self._on_worker_finished)

        thread.started.connect(worker.run)
        # تنظيف آمن: عند انتهاء الـ worker، أوقف الـ thread
        worker.finished.connect(thread.quit)
        # عند انتهاء الـ thread فعلاً (event loop خرج)، احذف الـ worker والـ thread
        thread.finished.connect(worker.deleteLater)
        thread.finished.connect(thread.deleteLater)
        # وأزِلهما من القواميس
        thread.finished.connect(lambda tid=task.task_id: self._cleanup(tid))

        self._workers[task.task_id] = worker
        self._threads[task.task_id] = thread
        thread.start()

    def _cleanup(self, task_id: int):
        """تُستدعى بعد thread.finished لإزالة المراجع بأمان."""
        should_try = False
        with QMutexLocker(self._mutex):
            self._workers.pop(task_id, None)
            self._threads.pop(task_id, None)
            if task_id in self._resume_after_cleanup:
                self._resume_after_cleanup.discard(task_id)
                if task_id not in self._pending and self._states.get(task_id) == STATUS_PENDING:
                    self._pending.append(task_id)
                should_try = True
        if should_try and not self._shutting_down:
            QTimer.singleShot(0, self._try_start_pending)

    # ------------------------- استقبال نهاية المهمة ------------------------ #
    def _on_worker_finished(self, task_id: int, success: bool):
        with QMutexLocker(self._mutex):
            cur_state = self._states.get(task_id)
            # عند الضغط Resume بسرعة بعد Pause يكون العامل القديم ما زال ينهي نفسه؛
            # لا نعتبر نهايته فشلاً، بل نُبقي المهمة Pending لتبدأ بعد cleanup.
            if task_id in self._resume_after_cleanup and cur_state == STATUS_PENDING and not success:
                final_state = STATUS_PENDING
            elif cur_state == STATUS_PAUSED:
                final_state = STATUS_PAUSED
            elif cur_state == STATUS_CANCELLED:
                final_state = STATUS_CANCELLED
            elif success:
                self._states[task_id] = STATUS_DONE
                final_state = STATUS_DONE
            else:
                self._states[task_id] = STATUS_ERROR
                final_state = STATUS_ERROR
            task_ref = self._tasks.get(task_id)
        # حدّث السجل بالحالة النهائية (ولا نسجل Pending المؤقت الناتج عن Resume السريع)
        if task_ref is not None and final_state != STATUS_PENDING:
            self.record_history(task_ref, final_state)

        self.task_state_changed.emit(task_id, final_state)
        self.task_finished.emit(task_id, success)
        if not self._shutting_down:
            self._try_start_pending()

    # ------------------------- Pause / Resume / Cancel --------------------- #
    def pause(self, task_id: int):
        task_ref = None
        with QMutexLocker(self._mutex):
            state = self._states.get(task_id)
            worker = self._workers.get(task_id)
            task_ref = self._tasks.get(task_id)
            if state == STATUS_RUNNING and worker is not None:
                worker.request_pause()
                self._states[task_id] = STATUS_PAUSED
            elif state == STATUS_PENDING:
                if task_id in self._pending:
                    self._pending.remove(task_id)
                self._states[task_id] = STATUS_PAUSED
        if task_ref is not None:
            self.record_history(task_ref, STATUS_PAUSED)
        self.task_state_changed.emit(task_id, STATUS_PAUSED)

    def resume(self, task_id: int):
        """استئناف مهمة موقوفة — تُعاد لقائمة الانتظار وتبدأ من جديد."""
        with QMutexLocker(self._mutex):
            task = self._tasks.get(task_id)
            if task is None:
                return
            state = self._states.get(task_id)
            if state not in (STATUS_PAUSED, STATUS_ERROR):
                return
            self._states[task_id] = STATUS_PENDING
            if task_id not in self._pending:
                self._pending.append(task_id)
            wait_old_worker = task_id in self._workers
            if wait_old_worker:
                self._resume_after_cleanup.add(task_id)
        self.task_state_changed.emit(task_id, STATUS_PENDING)
        if not wait_old_worker:
            self._try_start_pending()

    def cancel(self, task_id: int, delete_partial: bool = False):
        with QMutexLocker(self._mutex):
            task = self._tasks.get(task_id)
            state = self._states.get(task_id)
            worker = self._workers.get(task_id)

            if worker is not None and state == STATUS_RUNNING:
                worker.request_cancel()
            if task_id in self._pending:
                self._pending.remove(task_id)
            self._states[task_id] = STATUS_CANCELLED

        # حذف ملفات part اختيارياً
        if delete_partial and task is not None:
            try:
                for fp in glob.glob(task.output_path + "*"):
                    if fp.endswith(".part") or fp.endswith(".ytdl"):
                        os.remove(fp)
            except Exception as e:
                print(f"[cancel] فشل حذف الملفات الجزئية: {e}")

        if task is not None:
            self.record_history(task, STATUS_CANCELLED)
        self.task_state_changed.emit(task_id, STATUS_CANCELLED)

    def remove_task(self, task_id: int, delete_partial: bool = False):
        """إزالة المهمة كلياً من المدير (تستخدم بعد الانتهاء أو الإلغاء) بدون تغيير حالة السجل للمنتهية."""
        with QMutexLocker(self._mutex):
            state = self._states.get(task_id)
        if state in (STATUS_RUNNING, STATUS_PENDING, STATUS_PAUSED):
            self.cancel(task_id, delete_partial=delete_partial)
        with QMutexLocker(self._mutex):
            if task_id in self._pending:
                try:
                    self._pending.remove(task_id)
                except ValueError:
                    pass
            self._tasks.pop(task_id, None)
            self._states.pop(task_id, None)

    # ----------------------------- استعلام ---------------------------------- #
    def get_task(self, task_id: int) -> Optional[DownloadTask]:
        return self._tasks.get(task_id)

    def get_state(self, task_id: int) -> Optional[str]:
        return self._states.get(task_id)

    # ----------------------------- History (السجل) --------------------------- #
    def _load_history(self):
        """تحميل السجل من القرص."""
        try:
            if os.path.exists(HISTORY_FILE):
                with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                    self._history = json.load(f)
                if not isinstance(self._history, list):
                    self._history = []
        except Exception as e:
            print(f"[history] فشل تحميل السجل: {e}")
            self._history = []

    def _save_history(self):
        """حفظ السجل إلى القرص بطريقة آمنة (ذرية)."""
        try:
            # احتفظ بآخر MAX_HISTORY سجل فقط
            data = self._history[-MAX_HISTORY:]
            _atomic_write_text(HISTORY_FILE, json.dumps(data, ensure_ascii=False, indent=2))
        except Exception as e:
            print(f"[history] فشل حفظ السجل: {e}")

    def record_history(self, task: DownloadTask, status: str):
        """تسجيل/تحديث سجل لمهمة معينة."""
        # ابحث عن سجل سابق بنفس الـ url + output_path
        entry = None
        for h in self._history:
            if h.get("url") == task.url and h.get("output_path") == task.output_path \
                    and h.get("format_id") == task.format_id:
                entry = h
                break
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if entry is None:
            entry = {
                "url": task.url,
                "format_id": task.format_id,
                "output_path": task.output_path,
                "display_name": task.display_name,
                "thumbnail_url": getattr(task, "thumbnail_url", ""),
                "flag": dict(task.flag or {}),
                "added_at": now,
                "updated_at": now,
                "status": status,
            }
            self._history.append(entry)
        else:
            entry["status"] = status
            entry["updated_at"] = now
            entry["display_name"] = task.display_name or entry.get("display_name", "")
            if getattr(task, "thumbnail_url", ""):
                entry["thumbnail_url"] = task.thumbnail_url
        self._save_history()

    def get_history(self) -> List[dict]:
        """قائمة كل التحميلات السابقة (نسخة)."""
        return list(self._history)

    def clear_history(self):
        """مسح السجل بالكامل."""
        self._history = []
        self._save_history()

    def remove_history_entry(self, index: int):
        """حذف سجل واحد بحسب فهرسه في القائمة."""
        try:
            if 0 <= index < len(self._history):
                self._history.pop(index)
                self._save_history()
        except Exception:
            pass

    def retry_from_history(self, entry: dict):
        """إعادة تحميل من سجل سابق."""
        task = DownloadTask(
            url=entry.get("url", ""),
            format_id=entry.get("format_id", ""),
            output_path=entry.get("output_path", ""),
            flag=dict(entry.get("flag") or {}),
            display_name=entry.get("display_name", "") or os.path.basename(
                entry.get("output_path", "")
            ),
            thumbnail_url=entry.get("thumbnail_url", ""),
        )
        self.add_task(task)
        return task

    def shutdown(self):
        """إغلاق كل الـ threads بأمان عند الخروج من التطبيق."""
        self._shutting_down = True
        with QMutexLocker(self._mutex):
            self._pending.clear()
        for tid, worker in list(self._workers.items()):
            try:
                worker.request_cancel()
            except Exception:
                pass
        # إعطاء الـ threads فرصة للانتهاء بدون تدمير QThread وهو يعمل.
        deadline = time.time() + 8
        for tid, th in list(self._threads.items()):
            try:
                remaining = max(100, int((deadline - time.time()) * 1000))
                if th.isRunning():
                    th.quit()
                    th.wait(remaining)
            except Exception:
                pass


# ----------------------------- Queue (قائمة الانتظار) ----------------------- #
# ميزة جديدة (4.2): التقاط أي رابط يُنسخ إلى الحافظة تلقائياً أثناء عمل
# البرنامج، وتحليله في الخلفية (عنوان + صورة + التنسيقات المتاحة) دون أي
# تدخل من المستخدم، تمهيداً لعرضه في نافذة "قائمة الانتظار" حيث يمكن نسخ
# رابطه أو فتحه في المتصفح أو تحميله بجودة مختارة أو حذفه من القائمة.

_queue_id_counter = itertools.count(1)


@dataclass
class QueueItem:
    """عنصر واحد في قائمة الانتظار (رابط تم نسخه وجارٍ تحليله أو تم تحليله)."""
    url: str
    item_id: int = field(default_factory=lambda: next(_queue_id_counter))
    status: str = "analyzing"          # analyzing / ready / error
    title: str = ""
    thumbnail_url: str = ""
    duration: int = 0
    error_msg: str = ""
    audio: dict = field(default_factory=dict)
    video: dict = field(default_factory=dict)
    video_audio: dict = field(default_factory=dict)

    @property
    def display_title(self) -> str:
        return self.title or self.url


class QueueAnalyzeWorker(QObject):
    """يحلل رابطاً واحداً في الخلفية (Thread منفصل) بلا أي تأثير على الواجهة."""
    finished = pyqtSignal(int, object)   # item_id, (audio, video, video_audio, info_url)
    error = pyqtSignal(int, str)         # item_id, رسالة الخطأ

    def __init__(self, item_id: int, url: str):
        super().__init__()
        self.item_id = item_id
        self.url = url

    def run(self):
        try:
            backend = YouTubeDownloader()
            flag = {"op": os.path.exists(COOKIES_FILE), "subtitle": False, "subtitle_lang": "ar"}

            # نفس مسار الشاشة الرئيسية تماماً للروابط العادية (يوتيوب):
            # fun_for_all يستعمل information ثم sort_video_qualities، ولذلك
            # يعيد نفس الجودات والأحجام المرتبة التي تعرضها الشاشة الرئيسية.
            # أما فيسبوك وساوندكلاود فتبقى على مسار التحليل الإجباري نفسه
            # الذي تستخدمه الشاشة الرئيسية عند تحويلهما إلى تبويب التنسيقات.
            if _is_force_platform(self.url):
                result = backend.information_force(self.url, flag)
            else:
                low_id, low_size, _high_id, _high_size, info = backend.fun_for_all(
                    self.url, flag
                )

                audio = {}
                for audio_idx in range(2):
                    if audio_idx < len(low_id) and low_id[audio_idx]:
                        size = low_size[audio_idx] if audio_idx < len(low_size) else 0
                        audio[audio_idx] = [0, low_id[audio_idx], size]

                video = {}
                for quality_idx, quality in enumerate((144, 240, 360, 480, 720, 1080), start=2):
                    if quality_idx < len(low_id) and low_id[quality_idx]:
                        size = low_size[quality_idx] if quality_idx < len(low_size) else 0
                        video[len(video)] = [quality, low_id[quality_idx], size]

                # fun_for_all يعيد [العنوان، الصورة، الوقت]، بينما
                # QueueManager يتعامل مع بنية information_force:
                # [العنوان، المدة بالثواني، الصورة]. نحولها هنا فقط
                # حتى تبقى بطاقة القائمة متوافقة مع الواجهة الرئيسية.
                duration = 0
                try:
                    hh, mm, ss = str(info[2] or "00:00:00").split(":")
                    duration = int(hh) * 3600 + int(mm) * 60 + int(float(ss))
                except (IndexError, TypeError, ValueError):
                    pass
                info_url = [
                    info[0] if len(info) > 0 else "",
                    duration,
                    info[1] if len(info) > 1 else "",
                ]
                result = (audio, video, {}, info_url)

            self.finished.emit(self.item_id, result)
        except Exception as e:
            self.error.emit(self.item_id, str(e))


class QueueManager(QObject):
    """
    Singleton — يراقب الحافظة (Clipboard) باستمرار طوال عمل البرنامج، وكل
    رابط جديد يُنسخ يُضاف تلقائياً إلى قائمة الانتظار ويُحلَّل في الخلفية،
    بصرف النظر عن التبويب المفتوح حالياً.
    """
    _instance: Optional["QueueManager"] = None

    item_added = pyqtSignal(object)      # QueueItem
    item_updated = pyqtSignal(object)    # QueueItem
    item_removed = pyqtSignal(int)       # item_id

    # أقصى عدد روابط تُحلَّل في نفس اللحظة بالتوازي؛ أي رابط إضافي يُضاف
    # لطابور انتظار داخلي ويبدأ تحليله تلقائياً بمجرد تحرر أحد الأماكن الثلاثة.
    MAX_PARALLEL_ANALYSIS = 3

    def __init__(self):
        super().__init__()
        if QueueManager._instance is not None:
            raise RuntimeError("استخدم QueueManager.instance()")
        self._items: Dict[int, QueueItem] = {}
        self._active_urls = set()
        self._last_clipboard = ""
        self._threads = []            # (thread, worker) قيد التحليل حالياً (بحد أقصى MAX_PARALLEL_ANALYSIS)
        self._pending_ids: List[int] = []  # item_id بانتظار توفر مكان للتحليل
        self._capture_enabled = bool(get_section("queue").get("capture_enabled", True))
        self._load_items()
        # مراقبة الحافظة كل 1.2 ثانية — كافية للاستجابة السريعة بلا استهلاك ملحوظ.
        self._timer = QTimer(self)
        self._timer.setInterval(1200)
        self._timer.timeout.connect(self._poll_clipboard)
        self._timer.start()

    @classmethod
    def instance(cls) -> "QueueManager":
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    # ------------------------- حفظ واستعادة قائمة الانتظار ------------------------- #
    @staticmethod
    def _indexed_dict(value) -> dict:
        """إعادة مفاتيح dict المفهرسة إلى أعداد صحيحة بعد قراءتها من JSON."""
        if not isinstance(value, dict):
            return {}
        restored = {}
        for key, entry in value.items():
            try:
                index = int(key)
            except (TypeError, ValueError):
                continue
            if isinstance(entry, (list, tuple)):
                restored[index] = list(entry)
        return restored

    @staticmethod
    def _item_to_dict(item: QueueItem) -> dict:
        return {
            "item_id": item.item_id,
            "url": item.url,
            "status": item.status,
            "title": item.title,
            "thumbnail_url": item.thumbnail_url,
            "duration": item.duration,
            "error_msg": item.error_msg,
            "audio": item.audio or {},
            "video": item.video or {},
            "video_audio": item.video_audio or {},
        }

    def _save_items(self):
        """حفظ القائمة الحالية ذرّياً حتى تبقى العناصر بين جلسات البرنامج."""
        try:
            payload = [self._item_to_dict(item) for item in self._items.values()]
            _atomic_write_text(QUEUE_FILE, json.dumps(payload, ensure_ascii=False, indent=2))
        except Exception as e:
            print(f"[queue] خطأ حفظ القائمة: {e}")

    def _load_items(self):
        """استعادة العناصر المحفوظة؛ التحليل غير المكتمل يُستأنف في الخلفية."""
        try:
            if not os.path.exists(QUEUE_FILE):
                return
            with open(QUEUE_FILE, "r", encoding="utf-8") as f:
                payload = json.load(f)
            if isinstance(payload, dict):
                payload = payload.get("items", [])
            if not isinstance(payload, list):
                return

            restored_items = []
            for data in payload:
                if not isinstance(data, dict):
                    continue
                url = (data.get("url") or "").strip()
                if not _is_valid_url(url) or url in self._active_urls:
                    continue
                item = QueueItem(url=url)
                item.status = data.get("status") if data.get("status") in (
                    "ready", "error", "playlist", "analyzing", "queued"
                ) else "error"
                if item.status == "error" and _looks_like_playlist_url(url):
                    item.status = "playlist"
                item.title = data.get("title") or ""
                item.thumbnail_url = data.get("thumbnail_url") or ""
                try:
                    item.duration = int(data.get("duration") or 0)
                except (TypeError, ValueError):
                    item.duration = 0
                item.error_msg = data.get("error_msg") or ""
                item.audio = self._indexed_dict(data.get("audio"))
                item.video = self._indexed_dict(data.get("video"))
                item.video_audio = self._indexed_dict(data.get("video_audio"))
                self._items[item.item_id] = item
                self._active_urls.add(url)
                restored_items.append(item)

            # لا يمكن ترك ثريدات جلسة سابقة في حالة analyzing/queued؛ نعيد
            # إدخالها في مسار التحليل المعتاد عند بدء البرنامج.
            for item in restored_items:
                if item.status in ("analyzing", "queued"):
                    self._enqueue_or_start(item)
        except Exception as e:
            print(f"[queue] خطأ استعادة القائمة: {e}")

    # ------------------------- إعداد التقاط الحافظة ------------------------- #
    def set_capture_enabled(self, enabled: bool):
        """تفعيل/إلغاء التقاط الروابط تلقائياً من الحافظة (لا يمس العناصر الحالية)."""
        self._capture_enabled = bool(enabled)

    def is_capture_enabled(self) -> bool:
        return self._capture_enabled

    # ------------------------- مراقبة الحافظة ------------------------- #
    def note_internal_copy(self, text: str):
        """تُستدعى عندما ينسخ البرنامج نفسه نصاً (مثل زر نسخ الرابط في بطاقة
        قائمة الانتظار) حتى لا يُعاد اعتبار هذا النص رابطاً جديداً من المستخدم."""
        self._last_clipboard = text or ""

    def _poll_clipboard(self):
        if not self._capture_enabled:
            return
        try:
            text = pyperclip.paste()
        except Exception:
            return
        text = (text or "").split("&")[0].strip()
        if not text or text == self._last_clipboard:
            return
        self._last_clipboard = text
        if not _is_valid_url(text):
            return
        if text in self._active_urls:
            return
        self.add_url(text)

    # ------------------------- إدارة العناصر --------------------------- #
    def add_url(self, url: str):
        url = (url or "").strip()
        if not _is_valid_url(url) or url in self._active_urls:
            return
        item = QueueItem(url=url)
        self._items[item.item_id] = item
        self._active_urls.add(url)
        self.item_added.emit(item)
        self._enqueue_or_start(item)

    def _enqueue_or_start(self, item: QueueItem):
        """يبدأ التحليل فوراً لو يوجد مكان شاغر (أقل من 3 تحليلات متوازية)،
        وإلا يضع الرابط في طابور الانتظار الداخلي حتى يتحرر مكان."""
        if len(self._threads) >= self.MAX_PARALLEL_ANALYSIS:
            item.status = "queued"
            self._pending_ids.append(item.item_id)
            self.item_updated.emit(item)
        else:
            self._start_analysis(item)

    def _start_analysis(self, item: QueueItem):
        item.status = "analyzing"
        thread = QThread()
        worker = QueueAnalyzeWorker(item.item_id, item.url)
        worker.moveToThread(thread)
        thread.started.connect(worker.run)
        worker.finished.connect(self._on_analyzed)
        worker.error.connect(self._on_analyze_error)
        worker.finished.connect(thread.quit)
        worker.error.connect(thread.quit)
        thread.finished.connect(worker.deleteLater)
        thread.finished.connect(thread.deleteLater)
        thread.finished.connect(lambda t=thread: self._cleanup_thread(t))
        self._threads.append((thread, worker))
        thread.start()

    def reanalyze(self, item_id: int):
        """إعادة تحليل عنصر موجود دون نسخ الرابط من المصدر مرة أخرى."""
        item = self._items.get(item_id)
        if item is None or item.status in ("analyzing", "queued"):
            return
        item.status = "analyzing"
        item.error_msg = ""
        item.audio = {}
        item.video = {}
        item.video_audio = {}
        self.item_updated.emit(item)
        self._enqueue_or_start(item)
        self._save_items()

    def _cleanup_thread(self, thread):
        self._threads = [(t, w) for (t, w) in self._threads if t is not thread]
        self._start_next_pending()

    def _start_next_pending(self):
        """يبدأ تحليل العنصر التالي في طابور الانتظار إن وُجد مكان شاغر."""
        while self._pending_ids and len(self._threads) < self.MAX_PARALLEL_ANALYSIS:
            item_id = self._pending_ids.pop(0)
            item = self._items.get(item_id)
            if item is None:
                continue
            self._start_analysis(item)
            self.item_updated.emit(item)

    def _on_analyzed(self, item_id: int, result):
        item = self._items.get(item_id)
        if item is None:
            return
        audio, video, video_audio, info_url = result
        if not audio and not video and not video_audio:
            item.status = "playlist" if _looks_like_playlist_url(item.url) else "error"
            item.error_msg = (
                "هذا الرابط يشير إلى قائمة فيديوهات. أضف رابط فيديو منفرداً للتحميل."
                if item.status == "playlist"
                else "تعذّر العثور على أي تنسيقات قابلة للتحميل لهذا الرابط."
            )
        else:
            item.status = "ready"
            item.audio, item.video, item.video_audio = audio, video, video_audio
        if info_url:
            item.title = info_url[0] or item.url
            item.duration = info_url[1] or 0
            item.thumbnail_url = info_url[2] or ""
        self._save_items()
        self.item_updated.emit(item)

    def _on_analyze_error(self, item_id: int, msg: str):
        item = self._items.get(item_id)
        if item is None:
            return
        item.status = "playlist" if _looks_like_playlist_url(item.url) else "error"
        item.error_msg = (
            "هذا الرابط يشير إلى قائمة فيديوهات. أضف رابط فيديو منفرداً للتحميل."
            if item.status == "playlist" else msg
        )
        self._save_items()
        self.item_updated.emit(item)

    def remove_item(self, item_id: int):
        item = self._items.pop(item_id, None)
        if item is not None:
            self._active_urls.discard(item.url)
        if item_id in self._pending_ids:
            self._pending_ids.remove(item_id)
        self._save_items()
        self.item_removed.emit(item_id)

    def clear_all(self):
        """يحذف كل عناصر القائمة دفعة واحدة (تُستخدم من زر «تفريغ القائمة»).
        أي تحليل لا يزال يعمل في الخلفية لعنصر محذوف يكمل عمله بأمان ثم
        يتجاهل نتيجته تلقائياً (self._items لن يحتوي على المعرّف بعد الآن)."""
        for item_id in list(self._items.keys()):
            self.remove_item(item_id)

    def get_items(self) -> List[QueueItem]:
        # الأحدث أولاً
        return list(reversed(list(self._items.values())))

    def count(self) -> int:
        return len(self._items)

    def shutdown(self):
        """إيقاف آمن عند إغلاق البرنامج: وقف مراقبة الحافظة وانتظار انتهاء
        كل خيوط التحليل النشطة قبل تدميرها، لتجنّب أي تعطّل مفاجئ."""
        try:
            self._timer.stop()
        except Exception:
            pass
        self._save_items()
        for (t, w) in list(self._threads):
            try:
                t.quit()
                t.wait(2500)
            except Exception:
                pass
        self._threads = []
        self._pending_ids = []


# امتدادات نريد استبعادها (ترجمة/مؤقتة) عند البحث عن الفيديو الأصلي
_SKIP_EXTS = (".srt", ".vtt", ".ass", ".ssa", ".sub", ".part", ".ytdl", ".json3", ".tmp")


def _resolve_media_file(path: str) -> str:
    """
    يحاول تحديد ملف الفيديو/الصوت الفعلي للمسار المعطى.
    - يستبعد ملفات الترجمة والمؤقتة.
    - يفضّل الملف الأكبر حجماً (لأنه الفيديو/الصوت).
    """
    if os.path.exists(path) and not path.lower().endswith(_SKIP_EXTS):
        return path

    import glob as _glob
    candidates = _glob.glob(path + ".*") or _glob.glob(path + "*")
    # استبعد ملفات الترجمة والمؤقتة
    candidates = [c for c in candidates if not c.lower().endswith(_SKIP_EXTS)]
    if not candidates:
        return path  # سيُكتشف الفشل لاحقاً
    # رتّب تنازلياً حسب الحجم وخذ الأكبر
    try:
        candidates.sort(key=lambda x: os.path.getsize(x) if os.path.exists(x) else 0,
                        reverse=True)
    except Exception:
        pass
    return candidates[0]


def _open_path(path: str):
    """فتح ملف/مجلد بشكل متعدد المنصات (يتجنّب فتح ملف الترجمة)."""
    if not path:
        return
    candidate = _resolve_media_file(path)
    if not os.path.exists(candidate):
        QMessageBox.warning(None, "ملف غير موجود", f"تعذّر العثور على:\n{path}")
        return
    try:
        if sys.platform.startswith("win"):
            os.startfile(candidate)  # type: ignore[attr-defined]
        else:
            QDesktopServices.openUrl(QUrl.fromLocalFile(candidate))
    except Exception as e:
        QMessageBox.warning(None, "خطأ", f"تعذّر فتح الملف:\n{e}")


# ----------------------------- CardThumbWorker ------------------------------ #
class CardThumbWorker(QObject):
    """تحميل وتجهيز صورة بطاقة التحميل في Thread منفصل حتى لا تتجمد الواجهة."""
    finished = pyqtSignal(bytes)

    def __init__(self, image_url: str, width: int = 104, height: int = 58):
        super().__init__()
        self.image_url = image_url or ""
        self.width = width
        self.height = height

    def run(self):
        if not self.image_url:
            self.finished.emit(b"")
            return
        try:
            cache_dir = CACHE_IMAGES_DIR
            os.makedirs(cache_dir, exist_ok=True)
            h = hashlib.md5(self.image_url.encode("utf-8")).hexdigest()
            cache_path = os.path.join(cache_dir, f"card_{h}_{self.width}x{self.height}.png")
            if os.path.exists(cache_path):
                with open(cache_path, "rb") as f:
                    self.finished.emit(f.read())
                return

            resp = requests.get(self.image_url, timeout=12)
            resp.raise_for_status()
            img = Image.open(BytesIO(resp.content)).convert("RGBA")
            try:
                resample = Image.Resampling.LANCZOS
            except AttributeError:
                resample = Image.LANCZOS
            img.thumbnail((self.width, self.height), resample)

            # قص/توسيط داخل مساحة ثابتة مع زوايا دائرية
            canvas = Image.new("RGBA", (self.width, self.height), (0, 0, 0, 0))
            x = (self.width - img.width) // 2
            y = (self.height - img.height) // 2
            canvas.paste(img, (x, y))
            mask = Image.new("L", (self.width, self.height), 0)
            draw = ImageDraw.Draw(mask)
            draw.rounded_rectangle((0, 0, self.width, self.height), radius=12, fill=255)
            canvas.putalpha(mask)
            bio = BytesIO()
            canvas.save(bio, format="PNG")
            data = bio.getvalue()
            try:
                with open(cache_path, "wb") as f:
                    f.write(data)
            except Exception:
                pass
            self.finished.emit(data)
        except Exception as e:
            print(f"[thumb] فشل تحميل صورة البطاقة: {e}")
            self.finished.emit(b"")


# ----------------------------- DownloadCard --------------------------------- #
class DownloadCard(QFrame):
    """بطاقة تحميل واحدة."""

    def __init__(self, task: DownloadTask, manager: DownloadManager, parent=None):
        super().__init__(parent)
        self.task = task
        self.manager = manager
        self.task_id = task.task_id
        self._state = STATUS_PENDING

        self.setObjectName("DownloadCard")
        self.setProperty("status", "pending")
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.setMinimumHeight(110)
        self.setMaximumHeight(136)

        outer = QVBoxLayout(self)
        outer.setContentsMargins(12, 8, 12, 8)
        outer.setSpacing(7)

        # ---- الصف العلوي: الاسم + الأزرار ----
        top_row = QHBoxLayout()
        top_row.setSpacing(8)

        self.name_label = QLabel(task.display_name)
        self.name_label.setStyleSheet("font-size: 19px; font-weight: bold; color: #F4F7FB;")
        self.name_label.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        self.name_label.setMaximumWidth(620)
        self.name_label.setWordWrap(False)
        self.name_label.setToolTip(task.output_path)
        self._raw_name = task.display_name

        self.status_label = QLabel("في الانتظار...")
        self.status_label.setObjectName("StatusChip")

        self.pause_btn = QPushButton("⏸️")
        self.pause_btn.setFixedSize(34, 28)
        self.pause_btn.setToolTip("إيقاف مؤقت / استئناف")
        self.pause_btn.clicked.connect(self._on_pause_clicked)

        self.cancel_btn = QPushButton("🗑️")
        self.cancel_btn.setFixedSize(34, 28)
        self.cancel_btn.setToolTip("إلغاء / حذف")
        self.cancel_btn.clicked.connect(self._on_cancel_clicked)

        self.open_file_btn = QPushButton("🎬")
        self.open_file_btn.setFixedSize(34, 28)
        self.open_file_btn.setToolTip("فتح الملف")
        self.open_file_btn.clicked.connect(self._on_open_file_clicked)
        self.open_file_btn.setEnabled(False)

        self.open_folder_btn = QPushButton("📂")
        self.open_folder_btn.setFixedSize(34, 28)
        self.open_folder_btn.setToolTip("فتح مجلد الوجهة")
        self.open_folder_btn.clicked.connect(self._on_open_folder_clicked)

        self.thumb_label = QLabel("صورة")
        self.thumb_label.setFixedSize(104, 58)
        self.thumb_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.thumb_label.setToolTip("صورة التحميل")
        self.thumb_label.setStyleSheet(
            "background-color: #1E1E21; color: #8FAFCC; border: 1px solid #5A8EC5; "
            "border-radius: 12px; font-size: 12px; font-weight: bold;"
        )

        top_row.addWidget(self.name_label, 1)
        top_row.addWidget(self.status_label)
        top_row.addWidget(self.open_file_btn)
        top_row.addWidget(self.open_folder_btn)
        top_row.addWidget(self.pause_btn)
        top_row.addWidget(self.cancel_btn)
        top_row.addWidget(self.thumb_label)
        outer.addLayout(top_row)

        # ---- الصف السفلي: شريط مختصر + الحجم + السرعة ----
        bottom_row = QHBoxLayout()
        bottom_row.setSpacing(10)
        self.progress_bar = QProgressBar()
        self.progress_bar.setObjectName("CompactProgress")
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setFixedWidth(310)
        bottom_row.addWidget(self.progress_bar, 0, Qt.AlignmentFlag.AlignVCenter)

        self.size_label = QLabel("الحجم: —")
        self.size_label.setObjectName("StreamSizeLabel")
        bottom_row.addWidget(self.size_label)

        self.speed_label = QLabel("")
        self.speed_label.setStyleSheet("color: #D0D0D0; font-size: 14px; font-weight: bold;")
        bottom_row.addWidget(self.speed_label)
        bottom_row.addStretch(1)
        outer.addLayout(bottom_row)

        self._apply_elide()
        self._start_thumbnail_load()

    def _start_thumbnail_load(self):
        """تشغيل تحميل الصورة المصغرة للبطاقة دون تعطيل الواجهة."""
        url = getattr(self.task, "thumbnail_url", "") or ""
        if not url:
            return
        self._thumb_thread = QThread()
        self._thumb_worker = CardThumbWorker(url)
        self._thumb_worker.moveToThread(self._thumb_thread)
        self._thumb_thread.started.connect(self._thumb_worker.run)
        self._thumb_worker.finished.connect(self._on_thumbnail_ready)
        self._thumb_worker.finished.connect(self._thumb_thread.quit)
        self._thumb_thread.finished.connect(self._thumb_worker.deleteLater)
        self._thumb_thread.finished.connect(self._thumb_thread.deleteLater)
        self._thumb_thread.start()

    def _on_thumbnail_ready(self, data: bytes):
        if not data:
            return
        pix = QPixmap()
        if pix.loadFromData(data):
            self.thumb_label.setPixmap(pix.scaled(
                self.thumb_label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            ))

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._apply_elide()

    def _apply_elide(self):
        try:
            fm = self.name_label.fontMetrics()
            avail = max(120, self.width() - 460)
            elided = fm.elidedText(self._raw_name, Qt.TextElideMode.ElideMiddle, avail)
            self.name_label.setText(elided)
        except Exception:
            self.name_label.setText(self._raw_name)

    # ---------------------- handlers ---------------------- #
    def _on_pause_clicked(self):
        if self._state == STATUS_RUNNING:
            self.manager.pause(self.task_id)
        elif self._state in (STATUS_PAUSED, STATUS_ERROR):
            self.manager.resume(self.task_id)

    def _on_cancel_clicked(self):
        self.manager.cancel(self.task_id, delete_partial=False)

    def _on_open_file_clicked(self):
        _open_path(self.task.output_path)

    def _on_open_folder_clicked(self):
        """فتح المجلد الذي يحوي الملف."""
        folder = os.path.dirname(self.task.output_path)
        if folder and os.path.exists(folder):
            try:
                if sys.platform.startswith("win"):
                    os.startfile(folder)  # type: ignore[attr-defined]
                else:
                    QDesktopServices.openUrl(QUrl.fromLocalFile(folder))
            except Exception as e:
                QMessageBox.warning(self, "خطأ", f"تعذّر فتح المجلد:\n{e}")
        else:
            QMessageBox.warning(self, "غير موجود", "مجلد الوجهة غير موجود.")

    def mousePressEvent(self, event):
        # عند الانتهاء، النقر على البطاقة يفتح الملف
        if self._state == STATUS_DONE and event.button() == Qt.MouseButton.LeftButton:
            _open_path(self.task.output_path)
        super().mousePressEvent(event)

    # ---------------------- slots from manager ------------ #
    def on_progress(self, percent: float):
        try:
            self.progress_bar.setValue(int(percent))
        except Exception:
            pass

    def on_status(self, text: str):
        self.status_label.setText(text)

    def on_speed(self, text: str):
        self.speed_label.setText(text)

    def on_size(self, downloaded_mb: float, total_mb: float, stream_type: str = ""):
        label = stream_type or "الملف"
        if total_mb > 0:
            self.size_label.setText(f"{label}: {downloaded_mb:.1f} / {total_mb:.1f} MB")
        elif downloaded_mb > 0:
            self.size_label.setText(f"{label}: {downloaded_mb:.1f} MB")

    def on_state(self, state: str):
        self._state = state
        if state == STATUS_RUNNING:
            self.setProperty("status", "running")
            self.pause_btn.setText("⏸️")
            self.pause_btn.setToolTip("إيقاف مؤقت")
            self.status_label.setText("جاري التحميل...")
            self.open_file_btn.setEnabled(False)
        elif state == STATUS_PENDING:
            self.setProperty("status", "pending")
            self.pause_btn.setText("⏸️")
            self.status_label.setText("في الانتظار...")
        elif state == STATUS_PAUSED:
            self.setProperty("status", "paused")
            self.pause_btn.setText("▶️")
            self.pause_btn.setToolTip("استئناف")
            self.status_label.setText("متوقف مؤقتاً")
            self.speed_label.setText("")
        elif state == STATUS_DONE:
            self.setProperty("status", "done")
            self.pause_btn.setEnabled(False)
            self.progress_bar.setValue(100)
            self.status_label.setText("✅ تم التحميل")
            self.speed_label.setText("")
            self.open_file_btn.setEnabled(True)
        elif state == STATUS_ERROR:
            self.setProperty("status", "error")
            self.pause_btn.setText("🔁")
            self.pause_btn.setToolTip("إعادة المحاولة")
            self.status_label.setText("❌ حدث خطأ")
            self.speed_label.setText("")
        elif state == STATUS_CANCELLED:
            self.setProperty("status", "error")
            self.pause_btn.setEnabled(False)
            self.status_label.setText("ألغي")
            self.speed_label.setText("")
        # أعد تطبيق QSS بعد تغيير property
        self.style().unpolish(self)
        self.style().polish(self)


# ----------------------------- QueueCard ------------------------------------ #
class QueueCard(QFrame):
    """بطاقة عنصر واحد داخل قائمة الانتظار — بنفس تصميم بطاقة التحميل."""

    reanalyze_requested = pyqtSignal(int)

    def __init__(self, item: QueueItem, manager: "QueueManager", parent=None):
        super().__init__(parent)
        self.item = item
        self.manager = manager

        # نفس اسم الكائن الذي تعتمد عليه بطاقة التحميل في QSS، لضمان نفس التصميم
        self.setObjectName("DownloadCard")
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.setMinimumHeight(110)
        self.setMaximumHeight(136)

        outer = QVBoxLayout(self)
        outer.setContentsMargins(12, 8, 12, 8)
        outer.setSpacing(7)

        # ---- الصف العلوي: الاسم + الحالة + الأزرار + الصورة ----
        top_row = QHBoxLayout()
        top_row.setSpacing(8)

        self.name_label = QLabel(item.display_title)
        self.name_label.setStyleSheet("font-size: 19px; font-weight: bold; color: #F4F7FB;")
        self.name_label.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        self.name_label.setMaximumWidth(500)
        self.name_label.setWordWrap(False)
        self.name_label.setToolTip(item.url)
        self._raw_name = item.display_title

        if item.status == "analyzing":
            _initial_status = "جاري التحليل..."
        elif item.status == "queued":
            _initial_status = "⏳ في الانتظار..."
        else:
            _initial_status = ""
        self.status_label = QLabel(_initial_status)
        self.status_label.setObjectName("StatusChip")

        self.copy_btn = QPushButton("📋")
        self.copy_btn.setFixedSize(34, 28)
        self.copy_btn.setToolTip("نسخ الرابط")
        self.copy_btn.clicked.connect(self._on_copy_clicked)

        self.open_btn = QPushButton("🌐")
        self.open_btn.setFixedSize(34, 28)
        self.open_btn.setToolTip("فتح في المتصفح")
        self.open_btn.clicked.connect(self._on_open_clicked)

        self.delete_btn = QPushButton("🗑️")
        self.delete_btn.setFixedSize(34, 28)
        self.delete_btn.setToolTip("حذف من القائمة")
        self.delete_btn.clicked.connect(self._on_delete_clicked)

        self.reanalyze_btn = QPushButton("🔄")
        self.reanalyze_btn.setFixedSize(34, 28)
        self.reanalyze_btn.setToolTip("إعادة تحليل الرابط")
        self.reanalyze_btn.clicked.connect(self._on_reanalyze_clicked)

        self.thumb_label = QLabel("صورة")
        self.thumb_label.setFixedSize(104, 58)
        self.thumb_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.thumb_label.setToolTip("صورة الفيديو")
        self.thumb_label.setStyleSheet(
            "background-color: #1E1E21; color: #8FAFCC; border: 1px solid #5A8EC5; "
            "border-radius: 12px; font-size: 12px; font-weight: bold;"
        )

        top_row.addWidget(self.name_label, 1)
        top_row.addWidget(self.status_label)
        top_row.addWidget(self.thumb_label)
        outer.addLayout(top_row)

        # ---- الصف السفلي: قائمة الجودات + زر التحميل ----
        bottom_row = QHBoxLayout()
        bottom_row.setSpacing(10)

        self.quality_combo = QComboBox()
        self.quality_combo.setMinimumWidth(240)
        self.quality_combo.setEnabled(False)
        bottom_row.addWidget(self.quality_combo, 1)

        # أزرار الإجراءات الرمزية بجانب زر التحميل في الصف السفلي.
        bottom_row.addWidget(self.copy_btn)
        bottom_row.addWidget(self.open_btn)
        bottom_row.addWidget(self.delete_btn)
        bottom_row.addWidget(self.reanalyze_btn)

        self.download_btn = QPushButton("تحميل")
        self.download_btn.setMinimumSize(96, 34)
        self.download_btn.setToolTip("تحميل بالجودة المختارة")
        self.download_btn.setEnabled(False)
        self.download_btn.clicked.connect(self._on_download_clicked)
        bottom_row.addWidget(self.download_btn)
        bottom_row.addStretch(1)
        outer.addLayout(bottom_row)

        self._apply_elide()
        self._start_thumbnail_load()
        if item.status not in ("analyzing", "queued"):
            self.refresh(item)

    # ---------------------- الصورة المصغّرة ---------------------- #
    def _start_thumbnail_load(self):
        # === السبب الحقيقي لتحطّم البرنامج عند فتح قائمة الانتظار ===
        # __init__ يستدعي هذه الدالة مرة، ثم قد يستدعي self.refresh(item)
        # مباشرة بعده (لو كان العنصر جاهزاً "ready" من قبل)، و refresh بدورها
        # تستدعي هذه الدالة مرة أخرى طالما لا تزال الصورة فارغة (وهي كذلك
        # فعلاً لأن الثريد الأول ما زال يعمل ولم ينتهِ بعد). النداء الثاني
        # كان يستبدل self._thumb_thread بكائن QThread جديد، فيفقد الثريد
        # الأول (الذي لا يزال يعمل فعلياً) آخر مرجع بايثون له ويُدمَّر
        # فجأة وهو يعمل ← "QThread: Destroyed while thread is still
        # running" ← تعطّل البرنامج بالكامل. الحل: لا نبدأ ثريداً جديداً
        # طالما هناك ثريد سابق لنفس البطاقة ما زال يعمل.
        existing = getattr(self, "_thumb_thread", None)
        if existing is not None:
            try:
                if existing.isRunning():
                    return
            except RuntimeError:
                # الكائن C++ للثريد السابق حُذف فعلاً؛ يمكن المتابعة بأمان.
                pass
        url = self.item.thumbnail_url or ""
        if not url:
            return
        self._thumb_thread = QThread()
        self._thumb_worker = CardThumbWorker(url)
        self._thumb_worker.moveToThread(self._thumb_thread)
        self._thumb_thread.started.connect(self._thumb_worker.run)
        self._thumb_worker.finished.connect(self._on_thumbnail_ready)
        self._thumb_worker.finished.connect(self._thumb_thread.quit)
        self._thumb_thread.finished.connect(self._thumb_worker.deleteLater)
        self._thumb_thread.finished.connect(self._thumb_thread.deleteLater)
        self._thumb_thread.start()

    def _on_thumbnail_ready(self, data: bytes):
        if not data:
            return
        pix = QPixmap()
        if pix.loadFromData(data):
            self.thumb_label.setPixmap(pix.scaled(
                self.thumb_label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            ))

    def stop_threads(self):
        """يُستدعى قبل حذف البطاقة نهائياً من قائمة الانتظار: ينتظر انتهاء
        ثريد تحميل الصورة المصغّرة إن كان لا يزال يعمل، بدل تركه يُدمَّر
        فجأة وهو يعمل (كان هذا سبب انغلاق البرنامج المفاجئ عند التعامل مع
        قائمة الانتظار)."""
        thread = getattr(self, "_thumb_thread", None)
        if thread is not None:
            try:
                if thread.isRunning():
                    thread.quit()
                    thread.wait(3000)
            except Exception:
                pass

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._apply_elide()

    def _apply_elide(self):
        try:
            fm = self.name_label.fontMetrics()
            avail = max(120, self.width() - 340)
            elided = fm.elidedText(self._raw_name, Qt.TextElideMode.ElideMiddle, avail)
            self.name_label.setText(elided)
        except Exception:
            self.name_label.setText(self._raw_name)

    # ---------------------- تحديث حالة العنصر ---------------------- #
    def refresh(self, item: QueueItem):
        self.item = item
        self._raw_name = item.display_title
        self.name_label.setToolTip(item.url)
        self._apply_elide()
        self.reanalyze_btn.setEnabled(item.status not in ("analyzing", "queued"))
        pix = self.thumb_label.pixmap()
        if pix is None or pix.isNull():
            self._start_thumbnail_load()

        if item.status == "queued":
            self.status_label.setText("⏳ في الانتظار...")
            self.status_label.setToolTip("سيبدأ التحليل تلقائياً بمجرد توفر مكان (حد أقصى 3 تحليلات متوازية).")
            self.quality_combo.setEnabled(False)
            self.download_btn.setEnabled(False)
        elif item.status == "analyzing":
            self.status_label.setText("جاري التحليل...")
            self.status_label.setToolTip("")
            self.quality_combo.clear()
            self.quality_combo.setEnabled(False)
            self.download_btn.setEnabled(False)
        elif item.status == "playlist":
            self.status_label.setText("قائمة")
            self.status_label.setToolTip(item.error_msg or "هذا الرابط قائمة فيديوهات وليس ملف فيديو منفرداً.")
            self.quality_combo.setEnabled(False)
            self.download_btn.setEnabled(False)
        elif item.status == "error":
            self.status_label.setText("❌ فشل التحليل")
            self.status_label.setToolTip(item.error_msg or "")
            self.quality_combo.setEnabled(False)
            self.download_btn.setEnabled(False)
        else:
            self.status_label.setText("✅ جاهز")
            self.status_label.setToolTip("")
            self._populate_qualities()
            has_items = self.quality_combo.count() > 0
            self.quality_combo.setEnabled(has_items)
            self.download_btn.setEnabled(has_items)

    def _populate_qualities(self):
        self.quality_combo.clear()

        # التنسيقات المدمجة (صوت + فيديو) تُعرض كما أعادها محلل الرابط.
        va = self.item.video_audio or {}
        for i in range(len(va)):
            v0, fid, sz = va[i]
            label = f"{v0} : {sz} MB" if isinstance(v0, str) else f"{v0 or '-'}p : {sz} MB"
            self.quality_combo.addItem(f"🎬 {label}", (fid, sz, "av"))

        # في نتيجة fun_for_all تكون audio[0] هي الجودة الأقل؛ أما في
        # التنسيقات الخام للروابط الخاصة فنستعمل أقل abr مع الحفاظ على
        # ترتيب audio[0] عندما تكون القيم غير متاحة (abr=0).
        au = self.item.audio or {}
        audio_entries = list(au.values())
        lowest_audio = None
        if audio_entries:
            def _audio_quality_key(entry):
                try:
                    abr_value = float(entry[0] or 0)
                except (TypeError, ValueError, IndexError):
                    abr_value = 0
                return (1 if abr_value <= 0 else 0, abr_value)

            lowest_audio = min(audio_entries, key=_audio_quality_key)

        # فيديوهات منفصلة عن الصوت: أضف أقل صوت إلى الحجم وإلى format_id
        # حتى يكون السلوك مطابقاً للتحميل من الشاشة الرئيسية.
        video = self.item.video or {}
        for i in range(len(video)):
            v0, video_fid, video_size = video[i]
            total_size = video_size or 0
            format_id = video_fid
            if lowest_audio is not None:
                audio_fid = lowest_audio[1]
                audio_size = lowest_audio[2] or 0
                can_merge = (
                    audio_fid and video_fid
                    and not str(audio_fid).startswith("direct:")
                    and not str(video_fid).startswith("direct:")
                )
                if can_merge:
                    format_id = f"{audio_fid}+{video_fid}"
                    total_size = round(total_size + audio_size, 2)

            label = f"{v0} : {total_size} MB" if isinstance(v0, str) else f"{v0 or '-'}p : {total_size} MB"
            self.quality_combo.addItem(f"🎬 {label}", (format_id, total_size, "av"))

        # الصوت يُضاف أخيراً كما كان في بطاقة القائمة سابقاً.
        for abr, fid, sz in audio_entries:
            try:
                abr_int = int(float(abr or 0))
            except (TypeError, ValueError):
                abr_int = 0
            label = f"صوت {abr_int}kbps : {sz} MB" if abr_int > 0 else f"صوت : {sz} MB"
            self.quality_combo.addItem(f"🎧 {label}", (fid, sz, "audio"))

    # ---------------------- الأزرار ---------------------- #
    def _on_reanalyze_clicked(self):
        self.reanalyze_requested.emit(self.item.item_id)

    def _on_copy_clicked(self):
        try:
            pyperclip.copy(self.item.url)
            self.manager.note_internal_copy(self.item.url)
        except Exception:
            pass

    def _on_open_clicked(self):
        try:
            QDesktopServices.openUrl(QUrl(self.item.url))
        except Exception:
            pass

    def _on_delete_clicked(self):
        self.manager.remove_item(self.item.item_id)

    def _build_selected_task(self):
        idx = self.quality_combo.currentIndex()
        if idx < 0:
            return None
        data = self.quality_combo.itemData(idx)
        if not data or len(data) < 3:
            return None
        fid, _size, kind = data
        try:
            paths = load_paths()
        except Exception:
            paths = {}
        path_audio = paths.get("path_audio", default_downloads_dir())
        path_video = paths.get("path_video", default_downloads_dir())

        backend = YouTubeDownloader()
        name = backend.clean_filename(self.item.title or "untitled")
        if kind == "audio":
            if _is_facebook_url(self.item.url):
                out = _facebook_video_output_path(path_audio, name, ".mp3")
            else:
                out = os.path.join(path_audio, f"{name}.mp3")
        elif _is_facebook_url(self.item.url):
            # فيديو Facebook يُحفظ دائماً mp4 وباسم مؤرخ لتفادي تكرار أسماء
            # فيديوهات متعددة مأخوذة من الصفحة نفسها.
            out = _facebook_video_output_path(path_video, name, ".mp4")
        else:
            # مسار فيديو الشاشة الرئيسية يُترك بلا امتداد؛ yt-dlp يحدد الامتداد
            # النهائي بعد الدمج وفق merge_output_format.
            out = os.path.join(path_video, name)

        return DownloadTask(
            url=self.item.url,
            format_id=str(fid),
            output_path=out,
            flag={"op": os.path.exists(COOKIES_FILE), "subtitle": False, "subtitle_lang": "ar"},
            display_name=os.path.basename(out) or name,
            thumbnail_url=self.item.thumbnail_url,
        )

    def _on_download_clicked(self):
        task = self._build_selected_task()
        if task is None:
            return
        DownloadManager.instance().add_task(task)
        # بعد إرسالها لمدير التحميلات، لم تعد بحاجة للبقاء في قائمة الانتظار
        self.manager.remove_item(self.item.item_id)


# ----------------------------- QueueDialog ----------------------------------- #
class QueueDialog(QDialog):
    """نافذة قائمة الانتظار — تعرض كل الروابط المنسوخة التي يتم تحليلها في الخلفية."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.manager = QueueManager.instance()
        self.cards: Dict[int, QueueCard] = {}

        self.setWindowTitle("🕒 قائمة الانتظار")
        queue_settings = get_section("queue")
        try:
            saved_width = max(500, int(queue_settings.get("width", 660)))
            saved_height = max(400, int(queue_settings.get("height", 540)))
        except (TypeError, ValueError):
            saved_width, saved_height = 660, 540
        self.resize(saved_width, saved_height)

        root = QVBoxLayout(self)
        root.setContentsMargins(12, 12, 12, 12)
        root.setSpacing(8)

        header = QLabel("قائمة الانتظار")
        header.setStyleSheet("font-size: 20px; font-weight: bold;")
        root.addWidget(header)

        hint = QLabel(
            "انسخ أي رابط فيديو أثناء استخدام البرنامج — سيُضاف هنا تلقائياً "
            "ويُحلَّل في الخلفية دون الحاجة لأي إجراء إضافي."
        )
        hint.setWordWrap(True)
        hint.setStyleSheet("color: #B0B0B0; font-size: 14px;")
        root.addWidget(hint)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_content = QWidget()
        self.cards_layout = QVBoxLayout(self.scroll_content)
        self.cards_layout.setSpacing(8)
        self.cards_layout.setContentsMargins(4, 4, 4, 4)

        self.empty_label = QLabel("لا توجد روابط في قائمة الانتظار حالياً.")
        self.empty_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.empty_label.setStyleSheet("color: #888; font-size: 18px; padding: 20px;")
        self.cards_layout.addWidget(self.empty_label)
        self.cards_layout.addStretch(1)
        self.scroll.setWidget(self.scroll_content)
        root.addWidget(self.scroll, 1)

        # ملاحظة: الزر يُخفي النافذة فقط (hide) بدل إغلاقها (accept) — راجع
        # closeEvent أدناه لشرح السبب (تجنّب تعطّل مفاجئ في البرنامج).
        btns_row = QHBoxLayout()
        btns_row.setSpacing(8)

        self.clear_all_btn = QPushButton("🗑️ تفريغ القائمة")
        self.clear_all_btn.setToolTip("حذف كل الروابط الموجودة حالياً في قائمة الانتظار")
        self.clear_all_btn.clicked.connect(self._on_clear_all_clicked)
        btns_row.addWidget(self.clear_all_btn)

        self.download_all_btn = QPushButton("تحميل")
        self.download_all_btn.setMinimumSize(130, 40)
        self.download_all_btn.setToolTip("تحميل كل العناصر الجاهزة بالجودة المحددة في كل بطاقة")
        self.download_all_btn.clicked.connect(self._on_download_all_clicked)
        btns_row.addWidget(self.download_all_btn)

        close_btn = QPushButton("إغلاق")
        close_btn.clicked.connect(self._hide_and_save)
        btns_row.addWidget(close_btn)

        root.addLayout(btns_row)

        for item in self.manager.get_items():
            self._add_card(item)
        self._update_empty()

        self.manager.item_added.connect(self._add_card)
        self.manager.item_updated.connect(self._update_card)
        self.manager.item_removed.connect(self._remove_card)
        self._update_download_all_btn()

    def _add_card(self, item: QueueItem):
        if item.item_id in self.cards:
            return
        card = QueueCard(item, self.manager)
        card.reanalyze_requested.connect(self.manager.reanalyze)
        self.cards[item.item_id] = card
        self.cards_layout.insertWidget(0, card)
        self._update_empty()
        self._update_download_all_btn()

    def _update_card(self, item: QueueItem):
        card = self.cards.get(item.item_id)
        if card is not None:
            card.refresh(item)
        self._update_download_all_btn()

    def _remove_card(self, item_id: int):
        card = self.cards.pop(item_id, None)
        if card is not None:
            # ننتظر انتهاء ثريد الصورة المصغّرة (إن كان يعمل) قبل حذف
            # البطاقة نهائياً، بدل تدميرها فجأة وهي تعمل في الخلفية.
            card.stop_threads()
            self.cards_layout.removeWidget(card)
            card.setParent(None)
            card.deleteLater()
        self._update_empty()
        self._update_download_all_btn()

    def _update_empty(self):
        self.empty_label.setVisible(len(self.cards) == 0)

    def _update_download_all_btn(self):
        ready = any(
            card.item.status == "ready" and card.quality_combo.count() > 0
            for card in self.cards.values()
        )
        self.download_all_btn.setEnabled(ready)

    def _on_download_all_clicked(self):
        tasks = []
        item_ids = []
        for card in list(self.cards.values()):
            if card.item.status != "ready":
                continue
            task = card._build_selected_task()
            if task is not None:
                tasks.append(task)
                item_ids.append(card.item.item_id)
        if not tasks:
            return
        manager = DownloadManager.instance()
        for task in tasks:
            manager.add_task(task)
        for item_id in item_ids:
            self.manager.remove_item(item_id)

    def _on_clear_all_clicked(self):
        if not self.cards:
            return
        answer = QMessageBox.question(
            self,
            "تفريغ قائمة الانتظار",
            f"سيتم حذف كل الروابط الموجودة حالياً في قائمة الانتظار ({len(self.cards)}) "
            "بما فيها ما لا يزال قيد التحليل. هل أنت متأكد؟",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )
        if answer == QMessageBox.StandardButton.Yes:
            self.manager.clear_all()

    def _save_size(self):
        try:
            update_section("queue", {"width": int(self.width()), "height": int(self.height())})
        except Exception:
            pass

    def _hide_and_save(self):
        self._save_size()
        self.hide()

    def closeEvent(self, event):
        """إخفاء النافذة مع حفظ أبعادها بدلاً من تدميرها."""
        self._save_size()
        event.ignore()
        self.hide()

    def shutdown_threads(self):
        """يُستدعى عند إغلاق البرنامج فعلياً: ينتظر انتهاء كل ثريدات الصور
        المصغّرة الخاصة ببطاقات قائمة الانتظار قبل إنهاء العملية."""
        for card in list(self.cards.values()):
            card.stop_threads()


# ----------------------------- DownloadsTab --------------------------------- #
class DownloadsTab(QWidget):
    """التبويب الذي يحوي بطاقات التحميل."""

    # signal لطلب التحويل إلى تبويب التحميل المتعدد من الـ MainWindow
    request_switch_to_self = pyqtSignal()
    request_switch_to_main = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.manager = DownloadManager.instance()
        self.cards = {}  # task_id -> DownloadCard

        # حمّل إعدادات المستخدم المحفوظة
        s = get_section("downloads")
        self.auto_switch = bool(s.get("auto_switch", False))
        saved_parallel = int(s.get("max_parallel", 3))
        # طبّق على المدير
        self.manager.set_max_parallel(saved_parallel)

        root = QVBoxLayout(self)
        root.setContentsMargins(10, 10, 10, 10)
        root.setSpacing(8)

        # شريط علوي
        header = QHBoxLayout()
        title = QLabel("التحميلات")
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        header.addWidget(title)
        header.addStretch(1)

        header.addWidget(QLabel("التوازي:"))
        self.spin = QSpinBox()
        self.spin.setRange(1, 10)
        self.spin.setValue(self.manager.max_parallel())

        def _on_parallel(v):
            self.manager.set_max_parallel(v)
            update_value("downloads", "max_parallel", int(v))

        self.spin.valueChanged.connect(_on_parallel)
        header.addWidget(self.spin)

        self.auto_switch_cb = QCheckBox("الانتقال التلقائي")
        self.auto_switch_cb.setToolTip(
            "عند تفعيله، الضغط على تحميل في أي تبويب آخر يفتح هذا التبويب فوراً."
        )
        # طبّق الحالة المحفوظة قبل ربط الإشارة
        self.auto_switch_cb.setChecked(self.auto_switch)
        self.auto_switch_cb.stateChanged.connect(self._on_auto_switch_changed)
        header.addWidget(self.auto_switch_cb)

        self.main_btn = QPushButton("🏠 الرئيسية")
        self.main_btn.setToolTip("الرجوع إلى الشاشة الرئيسية")
        self.main_btn.clicked.connect(self.request_switch_to_main.emit)
        header.addWidget(self.main_btn)

        self.history_btn = QPushButton("📜 السجل")
        self.history_btn.clicked.connect(self._open_history)
        header.addWidget(self.history_btn)

        self.clear_btn = QPushButton("🧹 إخفاء المنتهية")
        self.clear_btn.clicked.connect(self._clear_finished)
        header.addWidget(self.clear_btn)

        root.addLayout(header)

        # منطقة بطاقات قابلة للتمرير
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_content = QWidget()
        self.cards_layout = QVBoxLayout(self.scroll_content)
        self.cards_layout.setSpacing(8)
        self.cards_layout.setContentsMargins(4, 4, 4, 4)
        # placeholder عند عدم وجود تحميلات (يبقى أسفل البطاقات)
        self.empty_label = QLabel("لا توجد تحميلات حالياً. أضف تحميلات من تبويبات أخرى.")
        self.empty_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.empty_label.setStyleSheet("color: #888; font-size: 20px; padding: 20px;")
        # ترتيب الـ layout: [البطاقات الجديدة تُدرج هنا فوق] [empty_label] [stretch]
        self.cards_layout.addWidget(self.empty_label)
        self.cards_layout.addStretch(1)
        self.scroll.setWidget(self.scroll_content)
        root.addWidget(self.scroll, 1)

        # وصل إشارات المدير
        self.manager.task_added.connect(self._on_task_added)
        self.manager.task_progress.connect(self._on_progress)
        self.manager.task_status.connect(self._on_status)
        self.manager.task_speed.connect(self._on_speed)
        self.manager.task_size.connect(self._on_size)
        self.manager.task_state_changed.connect(self._on_state_changed)

    def _on_task_added(self, task: DownloadTask):
        if task.task_id in self.cards:
            return
        card = DownloadCard(task, self.manager)
        self.cards[task.task_id] = card
        # نُدخل البطاقة الجديدة في الأعلى (الموضع 0) — الأحدث أولاً
        self.cards_layout.insertWidget(0, card)
        self._update_empty_label()
        # لو الانتقال التلقائي مفعَّل، اطلب التحويل إلى هذا التبويب
        if self.auto_switch:
            self.request_switch_to_self.emit()

    def _on_progress(self, task_id: int, percent: float):
        c = self.cards.get(task_id)
        if c:
            c.on_progress(percent)

    def _on_status(self, task_id: int, text: str):
        c = self.cards.get(task_id)
        if c:
            c.on_status(text)

    def _on_speed(self, task_id: int, text: str):
        c = self.cards.get(task_id)
        if c:
            c.on_speed(text)

    def _on_size(self, task_id: int, downloaded_mb: float, total_mb: float, stream_type: str = ""):
        c = self.cards.get(task_id)
        if c:
            c.on_size(downloaded_mb, total_mb, stream_type)

    def _on_auto_switch_changed(self, state):
        self.auto_switch = bool(state)
        update_value("downloads", "auto_switch", bool(state))

    def _open_history(self):
        dlg = HistoryDialog(self.manager, self)
        dlg.exec()

    def _on_state_changed(self, task_id: int, state: str):
        c = self.cards.get(task_id)
        if c:
            c.on_state(state)
            if state == STATUS_CANCELLED:
                # إزالة البطاقة بعد لحظات
                self._remove_card(task_id)

    def _remove_card(self, task_id: int):
        c = self.cards.pop(task_id, None)
        if c is not None:
            self.cards_layout.removeWidget(c)
            c.setParent(None)
            c.deleteLater()
        self._update_empty_label()

    def _clear_finished(self):
        for tid in list(self.cards.keys()):
            st = self.manager.get_state(tid)
            if st in (STATUS_DONE, STATUS_ERROR, STATUS_CANCELLED):
                self.manager.remove_task(tid)
                self._remove_card(tid)

    def _update_empty_label(self):
        self.empty_label.setVisible(len(self.cards) == 0)


# ----------------------------- HistoryDialog -------------------------------- #
class HistoryDialog(QDialog):
    """نافذة عرض سجل التحميلات السابقة + إعادة التحميل."""

    STATUS_LABELS = {
        "done": "✅ تم",
        "error": "❌ خطأ",
        "cancelled": "🚫 ألغي",
        "paused": "⏸ موقوف",
        "running": "⬇ يحمّل",
        "pending": "🕓 ينتظر",
    }

    def __init__(self, manager: DownloadManager, parent=None):
        super().__init__(parent)
        self.manager = manager
        self.setWindowTitle("سجل التحميلات السابقة")
        self.resize(820, 520)

        root = QVBoxLayout(self)

        info = QLabel(
            "كل التحميلات السابقة (حتى غير المكتملة) — انقر مرّتين أو اضغط "
            "\"إعادة التحميل\" لإضافة المهمة مرة أخرى."
        )
        info.setWordWrap(True)
        info.setStyleSheet("color: #B0B0B0; padding: 4px;")
        root.addWidget(info)

        self.list_widget = QListWidget()
        self.list_widget.itemDoubleClicked.connect(self._on_double_click)
        root.addWidget(self.list_widget, 1)

        btns = QHBoxLayout()
        self.retry_btn = QPushButton("🔁 إعادة التحميل")
        self.retry_btn.setObjectName("PrimaryButton")
        self.retry_btn.clicked.connect(self._retry_selected)
        btns.addWidget(self.retry_btn)

        self.open_folder_btn = QPushButton("📂 فتح المجلد")
        self.open_folder_btn.clicked.connect(self._open_folder_selected)
        btns.addWidget(self.open_folder_btn)

        self.delete_btn = QPushButton("🗑 حذف من السجل")
        self.delete_btn.clicked.connect(self._delete_selected)
        btns.addWidget(self.delete_btn)

        btns.addStretch(1)

        self.clear_all_btn = QPushButton("🧹 مسح كل السجل")
        self.clear_all_btn.clicked.connect(self._clear_all)
        btns.addWidget(self.clear_all_btn)

        self.close_btn = QPushButton("إغلاق")
        self.close_btn.clicked.connect(self.accept)
        btns.addWidget(self.close_btn)

        root.addLayout(btns)

        self._refresh()

    def _refresh(self):
        """ملء القائمة من سجل المدير (الأحدث أولاً)."""
        self.list_widget.clear()
        history = self.manager.get_history()
        # نعرض من الأحدث للأقدم
        for idx in range(len(history) - 1, -1, -1):
            h = history[idx]
            status = h.get("status", "")
            label = self.STATUS_LABELS.get(status, status or "?")
            name = h.get("display_name") or os.path.basename(h.get("output_path", ""))
            when = h.get("updated_at") or h.get("added_at") or ""
            text = f"{label}  •  {name}  •  {when}"
            item = QListWidgetItem(text)
            # نخزّن الفهرس الأصلي في data role
            item.setData(Qt.ItemDataRole.UserRole, idx)
            item.setToolTip(
                f"الرابط: {h.get('url', '')}\n"
                f"المسار: {h.get('output_path', '')}\n"
                f"الصيغة: {h.get('format_id', '')}"
            )
            self.list_widget.addItem(item)

        if self.list_widget.count() == 0:
            empty = QListWidgetItem("لا يوجد سجل تحميلات بعد.")
            empty.setFlags(Qt.ItemFlag.NoItemFlags)
            self.list_widget.addItem(empty)

    def _selected_history_entry(self):
        items = self.list_widget.selectedItems()
        if not items:
            return None, None
        idx = items[0].data(Qt.ItemDataRole.UserRole)
        if idx is None:
            return None, None
        history = self.manager.get_history()
        if 0 <= idx < len(history):
            return idx, history[idx]
        return None, None

    def _on_double_click(self, item):
        self._retry_selected()

    def _retry_selected(self):
        idx, entry = self._selected_history_entry()
        if entry is None:
            QMessageBox.information(self, "لم يُحدّد", "اختر عنصراً من السجل أولاً.")
            return
        self.manager.retry_from_history(entry)
        QMessageBox.information(self, "تمت الإضافة",
                                "أُضيف التحميل من جديد إلى قائمة التحميلات.")
        self._refresh()

    def _open_folder_selected(self):
        idx, entry = self._selected_history_entry()
        if entry is None:
            return
        path = entry.get("output_path", "")
        folder = os.path.dirname(path) if path else ""
        if folder and os.path.exists(folder):
            try:
                if sys.platform.startswith("win"):
                    os.startfile(folder)  # type: ignore[attr-defined]
                else:
                    QDesktopServices.openUrl(QUrl.fromLocalFile(folder))
            except Exception as e:
                QMessageBox.warning(self, "خطأ", str(e))
        else:
            QMessageBox.warning(self, "غير موجود", "المجلد غير موجود على القرص.")

    def _delete_selected(self):
        idx, entry = self._selected_history_entry()
        if entry is None:
            return
        self.manager.remove_history_entry(idx)
        self._refresh()

    def _clear_all(self):
        reply = QMessageBox.question(
            self, "تأكيد", "هل تريد مسح كل السجل؟",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if reply == QMessageBox.StandardButton.Yes:
            self.manager.clear_history()
            self._refresh()


HELP_HTML = """
<style>
  body { font-family: Arial, Tahoma, sans-serif; color: #EEEEEE;
         background-color: #252422; line-height: 1.7; font-size: 16px; }
  h1 { color: #5A8EC5; border-bottom: 2px solid #3A6EA5; padding-bottom: 6px; }
  h2 { color: #5A8EC5; margin-top: 20px; border-right: 4px solid #3A6EA5;
       padding-right: 10px; }
  h3 { color: #B0D4F1; margin-top: 14px; }
  ul { margin-right: 20px; padding-right: 12px; }
  li { margin-bottom: 6px; }
  code, .kbd { background-color: #1E1E21; color: #B0F0B0; padding: 1px 6px;
               border-radius: 4px; font-family: Consolas, monospace; }
  .note { background-color: #2E2E33; border-right: 4px solid #B0840A;
          padding: 8px 12px; margin: 10px 0; border-radius: 6px; }
  .ok { color: #6FE090; font-weight: bold; }
  .warn { color: #E0B070; font-weight: bold; }
  .err { color: #E07070; font-weight: bold; }
  table { width: 100%; border-collapse: collapse; margin: 10px 0; }
  th, td { border: 1px solid #444; padding: 8px; text-align: right; }
  th { background-color: #3A3A40; color: #B0D4F1; }
</style>

<h1>📖 دليل استخدام MG v4</h1>

<p>
برنامج <b>MG v4</b> أداة شاملة لتحميل الفيديوهات والصوتيات من يوتيوب وفيسبوك
وساوندكلاود وأكثر من 1000 منصة، مع نظام تحميل متعدد متوازي، سجل تحميلات،
وميزات متقدمة للترجمة والدمج والترميز.
</p>

<h2>🗂 التبويبات الخمسة</h2>

<table>
  <tr><th>التبويب</th><th>الوظيفة</th></tr>
  <tr><td><b>الرئيسية</b></td><td>تحميل فيديو واحد من يوتيوب باختيار الجودة (Audio + 144p → 1080p).</td></tr>
  <tr><td><b>تحميل الجميع</b></td><td>تحميل من أي منصة (يوتيوب/فيسبوك/ساوندكلاود/...) بقوائم الصيغ المتاحة.</td></tr>
  <tr><td><b>تحميل قائمة</b></td><td>تحميل قائمة تشغيل (Playlist) كاملة باختيار النطاق والجودات.</td></tr>
  <tr><td><b>التحميلات</b></td><td>عرض كل التحميلات الحية + السجل + التحكم في التوازي.</td></tr>
  <tr><td><b>الإعدادات</b></td><td>كل خيارات البرنامج + تجديد الكوكيز + سجل الأخطاء + المساعدة + زر وظائف أخرى.</td></tr>
</table>

<h2>1️⃣ تبويب الرئيسية</h2>
<ol>
  <li>انسخ رابط فيديو يوتيوب إلى الحافظة.</li>
  <li>اضغط <span class="kbd">تحليل رابط التحميل</span>.</li>
  <li>ستظهر أزرار الجودات مع الأحجام؛ اضغط أي جودة لإرسال المهمة إلى
      <b>تبويب التحميلات</b>.</li>
</ol>
<h3>الخيارات المتاحة:</h3>
<ul>
  <li><b>صوت فائق الجودة</b>: يختار أعلى bitrate صوتي متاح.</li>
  <li><b>فيديو فائق الجودة</b>: يختار أعلى نسخة من كل جودة بصرية.</li>
  <li><b>إضافة الترجمة</b>: يحمّل ملف ترجمة بنفس اسم الفيديو
      (يفتح تلقائياً مع المشغلات).</li>
  <li><b>لغة الترجمة</b>: العربية أو الإنجليزية. إن لم تتوفر اللغة المختارة،
      تُحمَّل الأخرى احتياطياً (حتى لو ترجمة آلية).</li>
  <li><b>تضمين الكوكيز</b>: استخدم <code>yt_cookies.txt</code> لتحميل
      الفيديوهات المقيّدة (تحتاج تسجيل دخول).</li>
  <li><span class="kbd">🔄</span> ريسيت كامل للشاشة.</li>
  <li><span class="kbd">🎬</span> / <span class="kbd">🎧</span> لاختيار مسار
      الفيديو/الصوت (يُحفظ في <code>path.json</code>).</li>
</ol>

<h2>2️⃣ تبويب تحميل الجميع</h2>
<p>
نفس فكرة الرئيسية لكن للمنصات الأخرى. اختيار الجودة عبر 3 قوائم:
</p>
<ul>
  <li><b>التنسيقات المدمجة</b>: فيديو+صوت في ملف واحد.
      <span class="ok">يدعم فيسبوك بجودتي HD و SD تلقائياً.</span></li>
  <li><b>تنسيقات الفيديو</b>: فيديو فقط.</li>
  <li><b>تنسيقات الصوت</b>: صوت فقط
      (<span class="ok">يدعم ساوندكلاود بكل جودات الصوت المتاحة</span>).</li>
</ul>
<p>اختر تنسيقاً واحداً (أو صوت + فيديو معاً لدمجهما) ثم اضغط زر التحميل.</p>

<h2>3️⃣ تبويب تحميل قائمة</h2>
<ol>
  <li>انسخ رابط قائمة تشغيل يوتيوب.</li>
  <li>اضغط <span class="kbd">نسخ الرابط</span> لاستخراج الفيديوهات.</li>
  <li>اختر نطاق البداية/النهاية ثم <span class="kbd">تحليل النطاق</span>.</li>
  <li>لكل فيديو ستظهر شبكة 4×2 من الجودات (لا تمرير عرضي):
      <br>الصف الأول: Audio منخفض - Audio عالي - 144p - 240p
      <br>الصف الثاني: 360p - 480p - 720p - 1080p
  </li>
  <li>للاختيار السريع: اختر جودة معينة من القائمة المنسدلة في الأعلى ثم
      <span class="kbd">✔ تحديد الكل</span>.</li>
  <li>اضغط <span class="kbd">تحميل</span> فتُضاف كل العناصر المختارة كمهام
      منفصلة إلى تبويب التحميلات.</li>
  <li><span class="kbd">🔄 ريسيت</span> يمسح كل شيء.</li>
</ol>

<h2>4️⃣ تبويب التحميلات ⭐</h2>
<p>القلب النابض للبرنامج. يعرض بطاقات لكل تحميل بشريط تقدم وأزرار:</p>
<ul>
  <li><span class="kbd">⏸️</span> إيقاف مؤقت (يحتفظ بملف <code>.part</code>).</li>
  <li><span class="kbd">▶️</span> استئناف من حيث توقّف التحميل.</li>
  <li><span class="kbd">❌</span> إلغاء وإزالة البطاقة.</li>
  <li><span class="kbd">🎬</span> فتح الملف بعد الانتهاء (لا يفتح الترجمة).</li>
  <li><span class="kbd">📂</span> فتح مجلد الوجهة في أي وقت.</li>
</ul>

<h3>في شريط الرأس:</h3>
<ul>
  <li><b>التوازي (1-10)</b>: عدد التحميلات المتزامنة.
      المهام الزائدة تنتظر في طابور.</li>
  <li><b>الانتقال التلقائي</b>: عند تفعيله، أي تحميل جديد من أي تبويب آخر
      ينقلك تلقائياً لهذا التبويب لمتابعة التقدم.</li>
  <li><span class="kbd">📜 السجل</span>: يعرض كل التحميلات السابقة
      (الناجحة/الفاشلة/الموقوفة) مع إمكانية:
    <ul>
      <li>🔁 <b>إعادة التحميل</b> (أو نقر مزدوج).</li>
      <li>📂 فتح مجلد الوجهة.</li>
      <li>🗑 حذف من السجل.</li>
      <li>🧹 مسح كل السجل.</li>
    </ul>
  </li>
  <li><span class="kbd">🧹 إخفاء المنتهية</span>: لإزالة البطاقات الناجحة فقط.</li>
</ul>

<div class="note">
<b>💡 الحجم الكلي:</b> يظهر تراكمياً (فيديو + صوت) أثناء التحميل، ثم الحجم
النهائي للملف المدمج بعد الانتهاء.
</div>

<h2>5️⃣ نافذة وظائف أخرى</h2>
<h3>📼 الدمج:</h3>
<ol>
  <li>اختر ملف الفيديو.</li>
  <li>اختر ملف الصوت.</li>
  <li>اختر مجلد الحفظ.</li>
  <li>اضغط <span class="kbd">دمج الملفات</span> — يستخدم ffmpeg بدون
      إعادة ترميز (سريع جداً، لا فقدان جودة).</li>
</ol>

<h3>🎚 إعادة الترميز (MP3):</h3>
<ol>
  <li>اختر ملف أو عدة ملفات صوتية/فيديو.</li>
  <li>اختر مجلد الحفظ.</li>
  <li>اختر <b>Bitrate</b> (4k → 320k) و <b>Channels</b> (1 أحادي / 2 ستيريو).</li>
  <li>اضغط <span class="kbd">إعادة الترميز</span>.</li>
</ol>

<h2>6️⃣ تبويب الإعدادات</h2>
<ul>
  <li><b>تجديد الكوكيز</b>: يستخرج كوكيز يوتيوب من المتصفح المختار ويحفظها
      في <code>yt_cookies.txt</code>.
      <span class="warn">يجب إغلاق المتصفح أولاً وأن تكون مسجَّل الدخول.</span></li>
  <li><b>سجل الأخطاء</b>: يفتح <code>mylog.txt</code> الذي يحوي كل رسائل
      التشغيل والأخطاء.</li>
  <li><b>وظائف أخرى</b>: زر داخل الإعدادات يفتح نافذة الدمج والترميز.</li>
  <li><b>المساعدة</b>: هذه النافذة.</li>
</ul>

<h2>📁 الملفات التي ينشئها البرنامج</h2>
<table>
  <tr><th>الملف</th><th>الوظيفة</th></tr>
  <tr><td><code>path.json</code></td><td>مسارات حفظ الفيديو/الصوت/القائمة.</td></tr>
  <tr><td><code>path_merge.json</code></td><td>مسارات حفظ الدمج/الترميز.</td></tr>
  <tr><td><code>settings.json</code></td><td>كل إعدادات المستخدم (خانات الاختيار،
      التوازي، الانتقال التلقائي، ...).</td></tr>
  <tr><td><code>download_history.json</code></td><td>سجل التحميلات.</td></tr>
  <tr><td><code>yt_cookies.txt</code></td><td>كوكيز يوتيوب (إن تم تجديدها).</td></tr>
  <tr><td><code>mylog.txt</code></td><td>سجل الأخطاء والمعلومات.</td></tr>
  <tr><td><code>my_cache/</code></td><td>كاش معلومات الفيديوهات والصور المصغرة.</td></tr>
</table>

<h2>⚙️ نصائح وحيل</h2>
<ul>
  <li>لو ظهر خطأ في التحليل، احذف مجلد <code>my_cache/</code> ثم أعد المحاولة.</li>
  <li>لو فشل التحميل بسبب <span class="err">HTTP 400 / 403</span>، فعّل
      <b>تضمين الكوكيز</b> بعد تجديدها من تبويب الإعدادات.</li>
  <li>لو فشلت الترجمة بـ <span class="err">429 Too Many Requests</span>،
      انتظر دقائق ثم أعد المحاولة (البرنامج يتعامل معها تلقائياً
      بـ exponential backoff).</li>
  <li>لإيقاف التطبيق بأمان: استخدم زر الإغلاق العادي (X) — البرنامج
      يُغلق كل الـ threads بأمان.</li>
  <li>كل إعداد تُغيّره يُحفظ تلقائياً ويعود معك حين تُعيد فتح البرنامج.</li>
</ul>

<h2>🎯 اختصارات مفيدة</h2>
<ul>
  <li>نقر مزدوج على بطاقة منتهية = فتح الملف.</li>
  <li>نقر مزدوج على عنصر في السجل = إعادة التحميل.</li>
  <li>نقر على ليبل المسار = فتح المجلد.</li>
</ul>

<hr>
<p style="text-align: center; color: #888; margin-top: 20px;">
<b>MG v4</b> — برمجة <b>علي دسوقي محمد</b> — 2026<br>
هاتف: 01060234822 — والحمد لله رب العالمين 🌹
</p>
"""


class HelpDialog(QDialog):
    """نافذة المساعدة الشاملة."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("📖 دليل استخدام MG v4")
        self.resize(900, 650)
        self.setMinimumSize(700, 500)

        root = QVBoxLayout(self)
        root.setContentsMargins(10, 10, 10, 10)
        root.setSpacing(8)

        header = QLabel("📖 دليل استخدام البرنامج")
        header.setStyleSheet(
            "font-size: 22px; font-weight: bold; color: #5A8EC5; padding: 6px;"
        )
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        root.addWidget(header)

        self.text = QTextBrowser()
        self.text.setOpenExternalLinks(True)
        self.text.setHtml(HELP_HTML)
        # ضمن RTL، نُبقي محتوى HTML كما هو ولكن اتجاه الـ widget RTL
        self.text.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        root.addWidget(self.text, 1)

        btns = QHBoxLayout()
        btns.addStretch(1)
        self.close_btn = QPushButton("إغلاق")
        self.close_btn.setObjectName("PrimaryButton")
        self.close_btn.setMinimumWidth(150)
        self.close_btn.setMinimumHeight(40)
        self.close_btn.clicked.connect(self.accept)
        btns.addWidget(self.close_btn)
        btns.addStretch(1)
        root.addLayout(btns)


class CookiesWorker(QObject):
    finished = pyqtSignal(bool, str)  # success, message

    def __init__(self, browser):
        super().__init__()
        self.browser = browser

    def run(self):
        try:
            ok = refresh_cookies(self.browser if self.browser != "تلقائي" else None)
            if ok and os.path.exists(COOKIES_FILE):
                size = os.path.getsize(COOKIES_FILE)
                self.finished.emit(True, f"تم بنجاح. حجم الملف: {size} بايت.")
            else:
                self.finished.emit(False, "لم نتمكن من تجديد الكوكيز من أي متصفح متاح.\n"
                                          "تأكد من تسجيل دخولك في يوتيوب على المتصفح، "
                                          "وأن المتصفح مغلق.")
        except Exception as e:
            self.finished.emit(False, f"خطأ: {e}")


class SettingsTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._build_ui()

    # --------------------------- بناء الواجهة ----------------------------- #
    def _build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(14, 12, 14, 12)
        root.setSpacing(10)

        header = QLabel("⚙️ الإعدادات العامة - MG v4")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setStyleSheet("color: silver; font-size: 24px; font-weight: bold; padding: 8px;")
        root.addWidget(header)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        content = QWidget()
        self.settings_layout = QVBoxLayout(content)
        self.settings_layout.setContentsMargins(6, 6, 6, 6)
        self.settings_layout.setSpacing(10)
        self.scroll.setWidget(content)
        root.addWidget(self.scroll, 1)

        self._build_general_panel()
        self._build_main_panel()
        self._build_force_panel()
        self._build_list_panel()
        self._build_downloads_panel()
        self._build_queue_panel()
        self._build_paths_panel()
        self._build_functions_panel()
        self.settings_layout.addStretch(1)

        note = QLabel(
            "كل تغيير هنا يُحفظ تلقائياً. بعض الخيارات تظهر فوراً في الشاشات المفتوحة، "
            "والباقي يُستخدم مع أول تحليل/تحميل جديد."
        )
        note.setWordWrap(True)
        note.setAlignment(Qt.AlignmentFlag.AlignCenter)
        note.setStyleSheet("color: #B0B0B0; font-size: 14px; padding: 4px;")
        root.addWidget(note)

    def showEvent(self, event):
        super().showEvent(event)
        self._refresh_from_settings()

    def _refresh_from_settings(self):
        """تحديث عناصر شاشة الإعدادات من القيم المحفوظة عند فتح التبويب."""
        try:
            main = get_section("main")
            force = get_section("force")
            lst = get_section("list")
            down = get_section("downloads")
            st = get_section("settings")
            funcs = get_section("functions")
            self._set_widget_checked(self.main_high_audio, main.get("high_audio", False))
            self._set_widget_checked(self.main_high_video, main.get("high_video", False))
            self._set_widget_checked(self.main_subtitle, main.get("subtitle", False))
            self._set_widget_checked(self.main_cookies, main.get("cookies", False))
            self._set_combo_lang(self.main_lang, main.get("subtitle_lang", "ar"))

            self._set_widget_checked(self.force_subtitle, force.get("subtitle", False))
            self._set_widget_checked(self.force_cookies, force.get("cookies", False))
            self._set_combo_lang(self.force_lang, force.get("subtitle_lang", "ar"))

            self._set_widget_checked(self.list_high_audio, lst.get("high_audio", False))
            self._set_widget_checked(self.list_high_video, lst.get("high_video", False))
            self._set_widget_checked(self.list_subtitle, lst.get("subtitle", False))
            self._set_widget_checked(self.list_cookies, lst.get("cookies", False))
            self._set_combo_lang(self.list_lang, lst.get("subtitle_lang", "ar"))

            self.parallel_spin.blockSignals(True)
            self.parallel_spin.setValue(int(down.get("max_parallel", 3)))
            self.parallel_spin.blockSignals(False)
            self._set_widget_checked(self.auto_switch_chk, down.get("auto_switch", False))

            queue_s = get_section("queue")
            self._set_widget_checked(self.queue_capture_chk, queue_s.get("capture_enabled", True))

            self.browser_combo.blockSignals(True)
            idx = self.browser_combo.findText(st.get("cookies_browser", "تلقائي"))
            self.browser_combo.setCurrentIndex(idx if idx >= 0 else 0)
            self.browser_combo.blockSignals(False)

            self.bitrate_combo.blockSignals(True)
            self.bitrate_combo.setCurrentText(funcs.get("bitrate", "48k"))
            self.bitrate_combo.blockSignals(False)
            self.channels_combo.blockSignals(True)
            self.channels_combo.setCurrentText(funcs.get("channels", "2"))
            self.channels_combo.blockSignals(False)

            paths = load_paths()
            self.path_video_lbl.setText(paths.get("path_video", default_downloads_dir()))
            self.path_audio_lbl.setText(paths.get("path_audio", default_downloads_dir()))
            self.path_list_lbl.setText(paths.get("path_list", default_downloads_dir()))
        except Exception as e:
            print(f"[settings] refresh ui error: {e}")

    def _panel(self, title: str):
        frame = QFrame()
        frame.setObjectName("Panel")
        lay = QVBoxLayout(frame)
        lay.setContentsMargins(12, 10, 12, 10)
        lay.setSpacing(8)
        lbl = QLabel(title)
        lbl.setStyleSheet("font-size: 20px; font-weight: bold; color: #BFD7FF;")
        lbl.setAlignment(Qt.AlignmentFlag.AlignRight)
        lay.addWidget(lbl)
        self.settings_layout.addWidget(frame)
        return lay

    def _row(self, parent_layout):
        row = QHBoxLayout()
        row.setSpacing(10)
        parent_layout.addLayout(row)
        return row

    # --------------------------- لوحات الإعدادات --------------------------- #
    def _build_general_panel(self):
        lay = self._panel("عام / الكوكيز / المساعدة")

        row_browser = self._row(lay)
        row_browser.addWidget(QLabel("متصفح الكوكيز:"))
        self.browser_combo = QComboBox()
        self.browser_combo.addItems([
            "تلقائي", "chrome", "edge", "brave", "firefox", "opera", "chromium", "vivaldi"
        ])
        self.browser_combo.setFixedWidth(150)
        saved_browser = get_section("settings").get("cookies_browser", "تلقائي")
        idx = self.browser_combo.findText(saved_browser)
        if idx >= 0:
            self.browser_combo.setCurrentIndex(idx)
        self.browser_combo.currentTextChanged.connect(
            lambda t: update_value("settings", "cookies_browser", t)
        )
        row_browser.addWidget(self.browser_combo)
        row_browser.addStretch(1)

        btns = self._row(lay)
        self.functions_btn = QPushButton("🧰 وظائف أخرى")
        self.functions_btn.setObjectName("PrimaryButton")
        self.functions_btn.setMinimumHeight(48)
        self.functions_btn.clicked.connect(self._open_functions)

        self.help_btn = QPushButton("📖 المساعدة")
        self.help_btn.setObjectName("PrimaryButton")
        self.help_btn.setMinimumHeight(48)
        self.help_btn.clicked.connect(self._open_help)

        self.cookies_btn = QPushButton("🍪 تجديد الكوكيز")
        self.cookies_btn.setObjectName("PrimaryButton")
        self.cookies_btn.setMinimumHeight(48)
        self.cookies_btn.clicked.connect(self._refresh_cookies)

        self.log_btn = QPushButton("📜 سجل الأخطاء")
        self.log_btn.setObjectName("PrimaryButton")
        self.log_btn.setMinimumHeight(48)
        self.log_btn.clicked.connect(self._open_log)

        btns.addWidget(self.functions_btn)
        btns.addWidget(self.help_btn)
        btns.addWidget(self.cookies_btn)
        btns.addWidget(self.log_btn)

        hint = QLabel("ملاحظة: لتجديد الكوكيز يفضّل إغلاق المتصفح وأن تكون مسجلاً في يوتيوب.")
        hint.setWordWrap(True)
        hint.setStyleSheet("color: #B0B0B0; font-size: 14px;")
        lay.addWidget(hint)

    def _build_main_panel(self):
        s = get_section("main")
        lay = self._panel("خيارات الشاشة الرئيسية")
        row = self._row(lay)
        self.main_high_audio = self._check("صوت فائق الجودة", s.get("high_audio", False),
                                           lambda v: self._set_main_option("high_audio", v))
        self.main_high_video = self._check("فيديو فائق الجودة", s.get("high_video", False),
                                           lambda v: self._set_main_option("high_video", v))
        self.main_subtitle = self._check("إضافة الترجمة", s.get("subtitle", False),
                                         lambda v: self._set_main_option("subtitle", v))
        self.main_cookies = self._check("تضمين الكوكيز", s.get("cookies", False),
                                        lambda v: self._set_main_option("cookies", v))
        for w in (self.main_high_audio, self.main_high_video, self.main_subtitle, self.main_cookies):
            row.addWidget(w)
        row.addWidget(QLabel("لغة الترجمة:"))
        self.main_lang = self._lang_combo(s.get("subtitle_lang", "ar"),
                                          lambda lang: self._set_main_option("subtitle_lang", lang))
        row.addWidget(self.main_lang)
        row.addStretch(1)

    def _build_force_panel(self):
        s = get_section("force")
        lay = self._panel("خيارات تحميل الجميع")
        row = self._row(lay)
        self.force_subtitle = self._check("إضافة الترجمة", s.get("subtitle", False),
                                          lambda v: self._set_force_option("subtitle", v))
        self.force_cookies = self._check("تضمين الكوكيز", s.get("cookies", False),
                                         lambda v: self._set_force_option("cookies", v))
        row.addWidget(self.force_subtitle)
        row.addWidget(self.force_cookies)
        row.addWidget(QLabel("لغة الترجمة:"))
        self.force_lang = self._lang_combo(s.get("subtitle_lang", "ar"),
                                           lambda lang: self._set_force_option("subtitle_lang", lang))
        row.addWidget(self.force_lang)
        row.addStretch(1)

    def _build_list_panel(self):
        s = get_section("list")
        lay = self._panel("خيارات تحميل القوائم")
        row = self._row(lay)
        self.list_high_audio = self._check("صوت فائق الجودة", s.get("high_audio", False),
                                           lambda v: self._set_list_option("high_audio", v))
        self.list_high_video = self._check("فيديو فائق الجودة", s.get("high_video", False),
                                           lambda v: self._set_list_option("high_video", v))
        self.list_subtitle = self._check("إضافة الترجمة", s.get("subtitle", False),
                                         lambda v: self._set_list_option("subtitle", v))
        self.list_cookies = self._check("تضمين الكوكيز", s.get("cookies", False),
                                        lambda v: self._set_list_option("cookies", v))
        for w in (self.list_high_audio, self.list_high_video, self.list_subtitle, self.list_cookies):
            row.addWidget(w)
        row.addWidget(QLabel("لغة الترجمة:"))
        self.list_lang = self._lang_combo(s.get("subtitle_lang", "ar"),
                                          lambda lang: self._set_list_option("subtitle_lang", lang))
        row.addWidget(self.list_lang)
        row.addStretch(1)

    def _build_downloads_panel(self):
        s = get_section("downloads")
        lay = self._panel("خيارات التحميلات")
        row = self._row(lay)
        row.addWidget(QLabel("عدد التحميلات المتوازية:"))
        self.parallel_spin = QSpinBox()
        self.parallel_spin.setRange(1, 10)
        self.parallel_spin.setValue(int(s.get("max_parallel", 3)))
        self.parallel_spin.valueChanged.connect(self._set_parallel)
        row.addWidget(self.parallel_spin)
        self.auto_switch_chk = self._check("الانتقال التلقائي إلى شاشة التحميل", s.get("auto_switch", False),
                                           self._set_auto_switch)
        row.addWidget(self.auto_switch_chk)
        row.addStretch(1)

    def _build_queue_panel(self):
        s = get_section("queue")
        lay = self._panel("قائمة الانتظار")
        row = self._row(lay)
        self.queue_capture_chk = self._check(
            "التقاط الروابط تلقائياً من الحافظة في قائمة الانتظار",
            s.get("capture_enabled", True),
            self._set_queue_capture,
        )
        row.addWidget(self.queue_capture_chk)
        row.addStretch(1)
        hint = QLabel(
            "عند التفعيل (الافتراضي): أي رابط تنسخه أثناء عمل البرنامج يُضاف "
            "تلقائياً لقائمة الانتظار ويُحلَّل في الخلفية. عند الإلغاء: لن "
            "يُلتقط شيء تلقائياً، ويمكنك فقط استخدام أزرار التحليل المعتادة."
        )
        hint.setWordWrap(True)
        hint.setStyleSheet("color: #B0B0B0; font-size: 13px;")
        lay.addWidget(hint)

    def _build_paths_panel(self):
        lay = self._panel("مسارات الحفظ")
        paths = load_paths()
        self.path_video_lbl = QLabel(paths.get("path_video", default_downloads_dir()))
        self.path_audio_lbl = QLabel(paths.get("path_audio", default_downloads_dir()))
        self.path_list_lbl = QLabel(paths.get("path_list", default_downloads_dir()))
        for label in (self.path_video_lbl, self.path_audio_lbl, self.path_list_lbl):
            label.setObjectName("PathLabel")
            label.setWordWrap(True)

        for title, key, label in [
            ("🎬 مسار الفيديو", "self.path_video_btn", self.path_video_lbl),
            ("🎧 مسار الصوت", "self.path_audio_btn", self.path_audio_lbl),
            ("📃 مسار القوائم", "self.path_list_btn", self.path_list_lbl),
        ]:
            row = self._row(lay)
            btn = QPushButton(title)
            btn.clicked.connect(lambda _=False, k=key: self._choose_save_path(k))
            row.addWidget(btn)
            row.addWidget(label, 1)

    def _build_functions_panel(self):
        s = get_section("functions")
        lay = self._panel("خيارات وظائف أخرى")
        row = self._row(lay)
        row.addWidget(QLabel("Bitrate الافتراضي:"))
        self.bitrate_combo = QComboBox()
        self.bitrate_combo.addItems([
            "4k", "8k", "16k", "24k", "32k", "40k", "48k", "56k", "64k",
            "80k", "96k", "112k", "128k", "160k", "192k", "224k", "256k", "320k",
        ])
        self.bitrate_combo.setCurrentText(s.get("bitrate", "48k"))
        self.bitrate_combo.currentTextChanged.connect(lambda t: update_value("functions", "bitrate", t))
        row.addWidget(self.bitrate_combo)
        row.addWidget(QLabel("Channels:"))
        self.channels_combo = QComboBox()
        self.channels_combo.addItems(["1", "2"])
        self.channels_combo.setCurrentText(s.get("channels", "2"))
        self.channels_combo.currentTextChanged.connect(lambda t: update_value("functions", "channels", t))
        row.addWidget(self.channels_combo)
        row.addStretch(1)

    # --------------------------- أدوات عناصر التحكم ------------------------ #
    def _check(self, text, checked, callback):
        cb = QCheckBox(text)
        cb.setChecked(bool(checked))
        cb.stateChanged.connect(lambda st: callback(bool(st)))
        return cb

    def _lang_combo(self, lang, callback):
        combo = QComboBox()
        combo.addItem("العربية", "ar")
        combo.addItem("الإنجليزية", "en")
        combo.setFixedWidth(120)
        combo.setCurrentIndex(0 if lang == "ar" else 1)
        combo.currentIndexChanged.connect(lambda _: callback(combo.currentData() or "ar"))
        return combo

    def _page(self, key):
        try:
            return getattr(self.window(), "pages", {}).get(key)
        except Exception:
            return None

    def _set_widget_checked(self, widget, value):
        if widget is None:
            return
        try:
            widget.blockSignals(True)
            widget.setChecked(bool(value))
            widget.blockSignals(False)
        except Exception:
            pass

    def _set_combo_lang(self, combo, lang):
        if combo is None:
            return
        try:
            combo.blockSignals(True)
            combo.setCurrentIndex(0 if lang == "ar" else 1)
            combo.blockSignals(False)
        except Exception:
            pass

    # --------------------------- تطبيق الإعدادات على الشاشات --------------- #
    def _set_main_option(self, key, value):
        update_value("main", key, value)
        page = self._page("main")
        if not page:
            return
        if key == "high_audio":
            self._set_widget_checked(getattr(page, "high_audio_choice", None), value)
            page._refresh_buttons_text()
        elif key == "high_video":
            self._set_widget_checked(getattr(page, "high_video_choice", None), value)
            page._refresh_buttons_text()
        elif key == "subtitle":
            page.flag["subtitle"] = bool(value)
            self._set_widget_checked(getattr(page, "subtitle_cb", None), value)
        elif key == "cookies":
            page.flag["op"] = bool(value)
            self._set_widget_checked(getattr(page, "cookies_cb", None), value)
        elif key == "subtitle_lang":
            page.flag["subtitle_lang"] = value
            self._set_combo_lang(getattr(page, "subtitle_lang", None), value)

    def _set_force_option(self, key, value):
        update_value("force", key, value)
        page = self._page("force")
        if not page:
            return
        if key == "subtitle":
            page.flag["subtitle"] = bool(value)
            self._set_widget_checked(getattr(page, "subtitle_cb", None), value)
        elif key == "cookies":
            page.flag["op"] = bool(value)
            self._set_widget_checked(getattr(page, "cookies_cb", None), value)
        elif key == "subtitle_lang":
            page.flag["subtitle_lang"] = value
            self._set_combo_lang(getattr(page, "subtitle_lang", None), value)

    def _set_list_option(self, key, value):
        update_value("list", key, value)
        page = self._page("list")
        if not page:
            return
        if key == "high_audio":
            self._set_widget_checked(getattr(page, "high_audio_cb", None), value)
            page._refresh_labels()
        elif key == "high_video":
            self._set_widget_checked(getattr(page, "high_video_cb", None), value)
            page._refresh_labels()
        elif key == "subtitle":
            page.flag["subtitle"] = bool(value)
            self._set_widget_checked(getattr(page, "subtitle_cb", None), value)
        elif key == "cookies":
            page.flag["op"] = bool(value)
            self._set_widget_checked(getattr(page, "cookies_cb", None), value)
        elif key == "subtitle_lang":
            page.flag["subtitle_lang"] = value
            self._set_combo_lang(getattr(page, "subtitle_lang", None), value)

    def _set_parallel(self, value):
        update_value("downloads", "max_parallel", int(value))
        DownloadManager.instance().set_max_parallel(int(value))
        page = self._page("downloads")
        if page and getattr(page, "spin", None) is not None:
            try:
                page.spin.blockSignals(True)
                page.spin.setValue(int(value))
                page.spin.blockSignals(False)
            except Exception:
                pass

    def _set_auto_switch(self, value):
        update_value("downloads", "auto_switch", bool(value))
        page = self._page("downloads")
        if page:
            page.auto_switch = bool(value)
            self._set_widget_checked(getattr(page, "auto_switch_cb", None), value)

    def _set_queue_capture(self, value):
        update_value("queue", "capture_enabled", bool(value))
        QueueManager.instance().set_capture_enabled(bool(value))

    def _choose_save_path(self, key):
        path = QFileDialog.getExistingDirectory(self, "اختر مجلداً")
        if not path:
            return
        data = YouTubeDownloader().choice_path_back(key, path)
        self.path_video_lbl.setText(data.get("path_video", ""))
        self.path_audio_lbl.setText(data.get("path_audio", ""))
        self.path_list_lbl.setText(data.get("path_list", ""))
        for page_key in ("main", "force", "list"):
            page = self._page(page_key)
            if page and hasattr(page, "_load_paths"):
                try:
                    page._load_paths()
                except Exception:
                    pass

    # --------------------------- الأزرار العامة ---------------------------- #
    def _refresh_cookies(self):
        self.cookies_btn.setEnabled(False)
        self.cookies_btn.setText("جاري التجديد...")
        browser = self.browser_combo.currentText()
        self._ck_thread = QThread()
        self._ck_worker = CookiesWorker(browser)
        self._ck_worker.moveToThread(self._ck_thread)
        self._ck_thread.started.connect(self._ck_worker.run)
        self._ck_worker.finished.connect(self._on_cookies_done)
        self._ck_worker.finished.connect(self._ck_thread.quit)
        self._ck_thread.finished.connect(self._ck_worker.deleteLater)
        self._ck_thread.finished.connect(self._ck_thread.deleteLater)
        self._ck_thread.start()

    def _on_cookies_done(self, success, msg):
        self.cookies_btn.setEnabled(True)
        self.cookies_btn.setText("🍪 تجديد الكوكيز")
        if success:
            QMessageBox.information(self, "تم", msg)
        else:
            QMessageBox.warning(self, "تعذّر", msg)

    def _open_functions(self):
        try:
            dlg = QDialog(self)
            dlg.setWindowTitle("🧰 وظائف أخرى")
            dlg.resize(820, 620)
            dlg.setMinimumSize(720, 520)
            lay = QVBoxLayout(dlg)
            lay.setContentsMargins(10, 10, 10, 10)
            lay.addWidget(FunctionsTab(dlg), 1)
            close_row = QHBoxLayout()
            close_row.addStretch(1)
            close_btn = QPushButton("إغلاق")
            close_btn.setObjectName("PrimaryButton")
            close_btn.setMinimumWidth(160)
            close_btn.clicked.connect(dlg.accept)
            close_row.addWidget(close_btn)
            close_row.addStretch(1)
            lay.addLayout(close_row)
            dlg.exec()
        except Exception as e:
            QMessageBox.warning(self, "خطأ", f"تعذّر فتح وظائف أخرى:\n{e}")

    def _open_help(self):
        try:
            dlg = HelpDialog(self)
            dlg.exec()
        except Exception as e:
            QMessageBox.warning(self, "خطأ", f"تعذّر فتح المساعدة:\n{e}")

    def _open_log(self):
        path = _app_data_path("mylog.txt")
        if not os.path.exists(path):
            QMessageBox.information(self, "السجل", "لا يوجد سجل أخطاء بعد.")
            return
        try:
            if sys.platform.startswith("win"):
                os.startfile(path)  # type: ignore[attr-defined]
            else:
                QDesktopServices.openUrl(QUrl.fromLocalFile(os.path.abspath(path)))
        except Exception as e:
            QMessageBox.warning(self, "خطأ", str(e))


PATH_FILE = _app_data_path("path_merge.json")


def _load_merge_paths():
    default = {
        "path_merge": os.path.join(os.path.expanduser("~"), "Downloads"),
        "path_codec": os.path.join(os.path.expanduser("~"), "Downloads"),
    }
    try:
        if os.path.exists(PATH_FILE):
            with open(PATH_FILE, "r", encoding="utf-8") as f:
                d = json.load(f)
            for k, v in default.items():
                d.setdefault(k, v)
            # تجاهل آمن لمفتاح tts إن وُجد قديماً
            d.pop("tts", None)
            return d
    except Exception:
        pass
    return default


def _save_merge_paths(d):
    try:
        # لا نكتب tts (محذوف)
        d = {k: v for k, v in d.items() if k != "tts"}
        _atomic_write_text(PATH_FILE, json.dumps(d, ensure_ascii=False, indent=4))
    except Exception as e:
        print(f"[functions_tab] save error: {e}")


# ----------------------------- FFmpeg worker ------------------------------- #
class FFmpegWorker(QObject):
    progress = pyqtSignal(str)  # نص حالة
    finished = pyqtSignal(bool, str)  # success, message

    def __init__(self, commands, success_msg):
        super().__init__()
        self.commands = commands  # list[list[str]]
        self.success_msg = success_msg

    def run(self):
        try:
            for cmd in self.commands:
                self.progress.emit(f"تنفيذ: {os.path.basename(cmd[-1])}")
                result = subprocess.run(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    creationflags=_CREATE_NO_WINDOW,
                )
                if result.returncode != 0:
                    err = result.stderr.decode(errors='ignore')[-500:]
                    self.finished.emit(False, f"خطأ ffmpeg:\n{err}")
                    return
            self.finished.emit(True, self.success_msg)
        except Exception as e:
            self.finished.emit(False, str(e))


# ----------------------------- FunctionsTab -------------------------------- #
class FunctionsTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.path_video = ""
        self.path_audio = ""
        self.codec_files = []  # list of files for codec

        data = _load_merge_paths()
        self.path_output = data["path_merge"]
        self.codec_path_output = data["path_codec"]
        self.data_path = data

        self._build_ui()

    def _build_ui(self):
        # حاوية رئيسية مع padding أكبر لتقصير العرض الفعلي للأقسام
        root = QVBoxLayout(self)
        root.setContentsMargins(12, 12, 12, 12)
        root.setSpacing(10)

        # نضع كل المحتوى في حاوية بعرض محدود (مركّز) لتقصير العرض
        wrapper = QHBoxLayout()
        wrapper.addStretch(1)
        center_col = QVBoxLayout()
        center_col.setSpacing(10)
        center_widget = QWidget()
        center_widget.setLayout(center_col)
        center_widget.setMaximumWidth(700)  # عرض أقصى = 700px للأقسام
        wrapper.addWidget(center_widget, 0, Qt.AlignmentFlag.AlignTop)
        wrapper.addStretch(1)
        root.addLayout(wrapper)

        # عرض ثابت للأزرار الجانبية، عرض محدود للـ labels
        BTN_W = 170
        LBL_MAX_W = 480

        # ------- قسم الدمج -------
        merge_box = QFrame()
        merge_box.setObjectName("Panel")
        m = QVBoxLayout(merge_box)
        m.setContentsMargins(10, 10, 10, 10)
        m.setSpacing(8)

        title = QLabel("🎞️ دمج الفيديو والصوت")
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        m.addWidget(title)

        r1 = QHBoxLayout()
        self.video_btn = QPushButton("اختر ملف الفيديو")
        self.video_btn.setFixedWidth(BTN_W)
        self.video_btn.clicked.connect(self._pick_video)
        self.video_lbl = QLabel("ملف الفيديو")
        self.video_lbl.setObjectName("PathLabel")
        self.video_lbl.setMaximumWidth(LBL_MAX_W)
        r1.addWidget(self.video_btn); r1.addWidget(self.video_lbl, 1)
        m.addLayout(r1)

        r2 = QHBoxLayout()
        self.audio_btn = QPushButton("اختر ملف الصوت")
        self.audio_btn.setFixedWidth(BTN_W)
        self.audio_btn.clicked.connect(self._pick_audio)
        self.audio_lbl = QLabel("ملف الصوت")
        self.audio_lbl.setObjectName("PathLabel")
        self.audio_lbl.setMaximumWidth(LBL_MAX_W)
        r2.addWidget(self.audio_btn); r2.addWidget(self.audio_lbl, 1)
        m.addLayout(r2)

        r3 = QHBoxLayout()
        self.merge_out_btn = QPushButton("اختر مجلد الحفظ")
        self.merge_out_btn.setFixedWidth(BTN_W)
        self.merge_out_btn.clicked.connect(self._pick_merge_output)
        self.merge_out_lbl = QLabel(self.path_output)
        self.merge_out_lbl.setObjectName("PathLabel")
        self.merge_out_lbl.setMaximumWidth(LBL_MAX_W)
        r3.addWidget(self.merge_out_btn); r3.addWidget(self.merge_out_lbl, 1)
        m.addLayout(r3)

        self.merge_btn = QPushButton("دمج الملفات")
        self.merge_btn.setObjectName("SuccessButton")
        self.merge_btn.setMinimumHeight(46)
        self.merge_btn.setFixedWidth(240)
        self.merge_btn.clicked.connect(self._do_merge)
        # توسيط الزر
        mbtn_row = QHBoxLayout()
        mbtn_row.addStretch(1)
        mbtn_row.addWidget(self.merge_btn)
        mbtn_row.addStretch(1)
        m.addLayout(mbtn_row)

        center_col.addWidget(merge_box)

        # ------- قسم إعادة الترميز -------
        codec_box = QFrame()
        codec_box.setObjectName("Panel")
        c = QVBoxLayout(codec_box)
        c.setContentsMargins(10, 10, 10, 10)
        c.setSpacing(8)

        ctitle = QLabel("🎚️ إعادة ترميز الصوت (mp3)")
        ctitle.setStyleSheet("font-size: 20px; font-weight: bold;")
        c.addWidget(ctitle)

        r4 = QHBoxLayout()
        self.codec_in_btn = QPushButton("اختر ملف الصوت")
        self.codec_in_btn.setFixedWidth(BTN_W)
        self.codec_in_btn.clicked.connect(self._pick_codec_inputs)
        self.codec_in_lbl = QLabel("ملف الصوت")
        self.codec_in_lbl.setObjectName("PathLabel")
        self.codec_in_lbl.setMaximumWidth(LBL_MAX_W)
        r4.addWidget(self.codec_in_btn); r4.addWidget(self.codec_in_lbl, 1)
        c.addLayout(r4)

        r5 = QHBoxLayout()
        self.codec_out_btn = QPushButton("اختر مجلد الحفظ")
        self.codec_out_btn.setFixedWidth(BTN_W)
        self.codec_out_btn.clicked.connect(self._pick_codec_output)
        self.codec_out_lbl = QLabel(self.codec_path_output)
        self.codec_out_lbl.setObjectName("PathLabel")
        self.codec_out_lbl.setMaximumWidth(LBL_MAX_W)
        r5.addWidget(self.codec_out_btn); r5.addWidget(self.codec_out_lbl, 1)
        c.addLayout(r5)

        r6 = QHBoxLayout()
        r6.addWidget(QLabel("Bitrate:"))
        self.bitrate_combo = QComboBox()
        self.bitrate_combo.setFixedWidth(110)
        self.bitrate_combo.addItems([
            "4k", "8k", "16k", "24k", "32k", "40k", "48k", "56k", "64k",
            "80k", "96k", "112k", "128k", "160k", "192k", "224k", "256k", "320k",
        ])
        # استرجاع الإعدادات المحفوظة
        _fs = get_section("functions")
        self.bitrate_combo.setCurrentText(_fs.get("bitrate", "48k"))
        self.bitrate_combo.currentTextChanged.connect(
            lambda t: update_value("functions", "bitrate", t)
        )
        r6.addWidget(self.bitrate_combo)
        r6.addSpacing(20)
        r6.addWidget(QLabel("Channels:"))
        self.channels_combo = QComboBox()
        self.channels_combo.setFixedWidth(70)
        self.channels_combo.addItems(["1", "2"])
        self.channels_combo.setCurrentText(_fs.get("channels", "2"))
        self.channels_combo.currentTextChanged.connect(
            lambda t: update_value("functions", "channels", t)
        )
        r6.addWidget(self.channels_combo)
        r6.addStretch(1)
        c.addLayout(r6)

        self.codec_btn = QPushButton("إعادة الترميز")
        self.codec_btn.setObjectName("SuccessButton")
        self.codec_btn.setMinimumHeight(46)
        self.codec_btn.setFixedWidth(240)
        self.codec_btn.clicked.connect(self._do_codec)
        cbtn_row = QHBoxLayout()
        cbtn_row.addStretch(1)
        cbtn_row.addWidget(self.codec_btn)
        cbtn_row.addStretch(1)
        c.addLayout(cbtn_row)

        center_col.addWidget(codec_box)
        center_col.addStretch(1)

    # --------------------------- pickers ---------------------------------- #
    def _pick_video(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "اختر ملف الفيديو", "",
            "Video files (*.mp4 *.mkv *.avi *.mov *.flv *.wmv *.webm)"
        )
        if path:
            self.path_video = path
            self.video_lbl.setText(os.path.basename(path))

    def _pick_audio(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "اختر ملف الصوت", "",
            "Audio files (*.mp3 *.wav *.aac *.flac *.ogg *.m4a *.wma)"
        )
        if path:
            self.path_audio = path
            self.audio_lbl.setText(os.path.basename(path))

    def _pick_merge_output(self):
        p = QFileDialog.getExistingDirectory(self, "اختر مجلد الحفظ")
        if p:
            self.path_output = p
            self.merge_out_lbl.setText(p)
            self.data_path["path_merge"] = p
            _save_merge_paths(self.data_path)

    def _pick_codec_inputs(self):
        # إصلاح خطأ القائمة الأصلي (الفاصلة المفقودة)
        files, _ = QFileDialog.getOpenFileNames(
            self, "اختر ملفات الصوت/الفيديو", "",
            "Audio files (*.mp3 *.wav *.aac *.flac *.ogg *.m4a *.wma);;"
            "Video files (*.mp4 *.mkv *.avi *.mov *.flv *.wmv *.webm);;"
            "All files (*.*)"
        )
        if files:
            self.codec_files = files
            if len(files) == 1:
                self.codec_in_lbl.setText(os.path.basename(files[0]))
            else:
                self.codec_in_lbl.setText(f"{len(files)} ملفات محددة")

    def _pick_codec_output(self):
        p = QFileDialog.getExistingDirectory(self, "اختر مجلد الحفظ")
        if p:
            self.codec_path_output = p
            self.codec_out_lbl.setText(p)
            self.data_path["path_codec"] = p
            _save_merge_paths(self.data_path)

    # --------------------------- actions ---------------------------------- #
    def _do_merge(self):
        if not (self.path_video and self.path_audio and self.path_output):
            QMessageBox.warning(self, "ناقص", "يرجى تحديد ملف فيديو وملف صوت ومجلد الحفظ.")
            return
        file_name = os.path.splitext(os.path.basename(self.path_video))[0]
        out_path = os.path.join(self.path_output, file_name + ".mp4")
        cmd = [
            FFMPEG,
            "-y",
            "-i", self.path_video,
            "-i", self.path_audio,
            "-c:v", "copy",
            "-c:a", "copy",
            "-map", "0:v:0",
            "-map", "1:a:0",
            "-shortest",
            out_path,
        ]
        self.merge_btn.setEnabled(False)
        self.merge_btn.setText("جاري الدمج...")
        self._run_ffmpeg([cmd], "تم الدمج بنجاح",
                         on_done=lambda ok, msg: self._after_merge(ok, msg, out_path))

    def _after_merge(self, ok, msg, out_path):
        self.merge_btn.setEnabled(True)
        self.merge_btn.setText("دمج الملفات")
        if ok:
            QMessageBox.information(self, "تم", f"{msg}\n{out_path}")
        else:
            QMessageBox.critical(self, "خطأ", msg)

    def _do_codec(self):
        if not (self.codec_files and self.codec_path_output):
            QMessageBox.warning(self, "ناقص", "يرجى تحديد الملفات ومجلد الحفظ.")
            return
        bitrate = self.bitrate_combo.currentText()
        ch = self.channels_combo.currentText()
        cmds = []
        for f in self.codec_files:
            name = os.path.splitext(os.path.basename(f))[0]
            out = os.path.join(self.codec_path_output, name + ".mp3")
            cmds.append([
                FFMPEG, "-y",
                "-i", f,
                "-c:a", "libmp3lame",
                "-ac", ch,
                "-ar", "22050",
                "-b:a", bitrate,
                out,
            ])
        self.codec_btn.setEnabled(False)
        self.codec_btn.setText("جاري الترميز...")
        self._run_ffmpeg(cmds, "تم الترميز بنجاح", on_done=self._after_codec)

    def _after_codec(self, ok, msg):
        self.codec_btn.setEnabled(True)
        self.codec_btn.setText("إعادة الترميز")
        if ok:
            QMessageBox.information(self, "تم", msg)
        else:
            QMessageBox.critical(self, "خطأ", msg)

    def _run_ffmpeg(self, cmds, success_msg, on_done):
        if not hasattr(self, "_active_threads"):
            self._active_threads = []
        thread = QThread()
        worker = FFmpegWorker(cmds, success_msg)
        worker.moveToThread(thread)
        thread.started.connect(worker.run)
        worker.finished.connect(on_done)
        worker.finished.connect(thread.quit)
        thread.finished.connect(worker.deleteLater)
        thread.finished.connect(thread.deleteLater)
        thread.finished.connect(lambda t=thread: self._cleanup_thread(t))
        self._active_threads.append((thread, worker))
        thread.start()
        return True

    def _cleanup_thread(self, thread):
        if hasattr(self, "_active_threads"):
            self._active_threads = [
                (t, w) for (t, w) in self._active_threads if t is not thread
            ]


MAIN_BACKEND = YouTubeDownloader()


def _validate_url(url: str) -> bool:
    return _is_valid_url(url)


# ----------------------------- Analyze Worker ------------------------------- #
class AnalyzeWorker(QObject):
    finished = pyqtSignal(object)  # tuple أو None
    error = pyqtSignal(str)

    def __init__(self, url, flag):
        super().__init__()
        self.url = url
        self.flag = flag

    def run(self):
        try:
            result = MAIN_BACKEND.fun_for_all(self.url, self.flag)
            # تحقق صحة النتيجة قبل البثّ
            if not result or len(result) < 5:
                self.error.emit("لم يرجع التحليل بيانات صالحة.")
                return
            ids, sizes, ids_h, sizes_h, info = result
            if not ids or not sizes:
                self.error.emit(
                    "لم يتم العثور على جودات صوت/فيديو لهذا الرابط.\n"
                    "تأكد أن الرابط صحيح وأن الفيديو متاح للعرض."
                )
                return
            self.finished.emit(result)
        except KeyError as ke:
            self.error.emit(
                f"بيانات الكاش ناقصة أو الفيديو لا يدعم هذا المفتاح: {ke}\n"
                "احذف مجلد my_cache وأعد المحاولة."
            )
        except Exception as e:
            import traceback
            traceback.print_exc()
            self.error.emit(f"{type(e).__name__}: {e}")


# ----------------------------- MainTab ------------------------------------- #
class MainTab(QWidget):
    request_force_analyze = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        # حمّل إعدادات المستخدم المحفوظة
        s = get_section("main")
        self.flag = {
            "op": bool(s.get("cookies", False)),
            "subtitle": bool(s.get("subtitle", False)),
            "subtitle_lang": s.get("subtitle_lang", "ar"),
        }
        self._saved_settings = s
        self.url = ""
        self.ids = []
        self.sizes = []
        self.ids_heigh = []
        self.sizes_heigh = []
        self.info_video = []

        self._build_ui()
        self._load_paths()

    # --------------------------- UI build --------------------------------- #
    def _build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(20, 16, 20, 16)
        root.setSpacing(10)

        self.analyze_btn = QPushButton("تحليل رابط التحميل")
        self.analyze_btn.setObjectName("PrimaryButton")
        self.analyze_btn.setMinimumHeight(60)
        self.analyze_btn.clicked.connect(self._start_analyze)
        root.addWidget(self.analyze_btn)

        # شبكة الجودات (4 أعمدة × صفوف)
        grid = QGridLayout()
        grid.setHorizontalSpacing(10)
        grid.setVerticalSpacing(10)

        self.low_audio_btn = self._make_quality_btn(" Audio : ")
        self.high_audio_btn = self._make_quality_btn(" Audio : ")
        self.b144p_btn = self._make_quality_btn(" 144p : ")
        self.b240p_btn = self._make_quality_btn(" 240p : ")
        self.b360p_btn = self._make_quality_btn(" 360p : ")
        self.b480p_btn = self._make_quality_btn(" 480p : ")
        self.b720p_btn = self._make_quality_btn(" 720p : ")
        self.b1080p_btn = self._make_quality_btn(" 1080p : ")

        self.quality_buttons = {
            "low_audio": self.low_audio_btn,
            "high_audio": self.high_audio_btn,
            "144p": self.b144p_btn,
            "240p": self.b240p_btn,
            "360p": self.b360p_btn,
            "480p": self.b480p_btn,
            "720p": self.b720p_btn,
            "1080p": self.b1080p_btn,
        }

        self.low_audio_btn.clicked.connect(lambda: self._press("low_audio"))
        self.high_audio_btn.clicked.connect(lambda: self._press("high_audio"))
        self.b144p_btn.clicked.connect(lambda: self._press("144p"))
        self.b240p_btn.clicked.connect(lambda: self._press("240p"))
        self.b360p_btn.clicked.connect(lambda: self._press("360p"))
        self.b480p_btn.clicked.connect(lambda: self._press("480p"))
        self.b720p_btn.clicked.connect(lambda: self._press("720p"))
        self.b1080p_btn.clicked.connect(lambda: self._press("1080p"))

        grid.addWidget(self.low_audio_btn, 0, 0)
        grid.addWidget(self.high_audio_btn, 0, 1)
        grid.addWidget(self.b144p_btn, 1, 0)
        grid.addWidget(self.b240p_btn, 1, 1)
        grid.addWidget(self.b360p_btn, 2, 0)
        grid.addWidget(self.b480p_btn, 2, 1)
        grid.addWidget(self.b720p_btn, 3, 0)
        grid.addWidget(self.b1080p_btn, 3, 1)

        root.addLayout(grid, 1)

        # عرض العنوان + الصورة + المدة (الوقت overlay فوق الصورة)
        info_row = QHBoxLayout()
        info_row.setSpacing(10)
        info_row.setContentsMargins(0, 0, 0, 0)

        self.title_label = QLabel(" سُبْحَانَ اللَّهِ وَبِحَمْدِهِ، سُبْحَانَ اللَّهِ الْعَظِيمِ")
        self.title_label.setObjectName("TitleLabel")
        self.title_label.setWordWrap(True)
        self.title_label.setFixedHeight(117)  # محاذاة مع الصورة
        self.title_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        info_row.addWidget(self.title_label, 3)

        # الصورة في حاوية لعرض overlay للوقت
        self.photo_container = QWidget()
        self.photo_container.setFixedSize(247, 117)
        self.photo_label = QLabel(self.photo_container)
        self.photo_label.setGeometry(0, 0, 247, 117)
        self.photo_label.setStyleSheet("background-color: silver; border-radius: 10px;")
        self.photo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # وقت الفيديو كـ overlay في الزاوية السفلى اليمنى
        self.time_label = QLabel("00:00:00", self.photo_container)
        self.time_label.setStyleSheet(
            "background-color: rgba(0, 0, 0, 180);"
            "color: white;"
            "font-weight: bold;"
            "font-size: 14px;"
            "padding: 2px 6px;"
            "border-radius: 4px;"
        )
        self.time_label.adjustSize()
        # ضعه في الزاوية اليمنى السفلى
        self.time_label.move(247 - self.time_label.width() - 6,
                             117 - self.time_label.height() - 6)
        self.time_label.raise_()

        info_row.addWidget(self.photo_container, 0, Qt.AlignmentFlag.AlignVCenter)
        root.addLayout(info_row)

        # خيارات
        opts_row = QHBoxLayout()
        self.high_audio_choice = QCheckBox("صوت فائق الجودة")
        self.high_video_choice = QCheckBox("فيديو فائق الجودة")
        self.subtitle_cb = QCheckBox("إضافة الترجمة")
        self.subtitle_lang = QComboBox()
        self.subtitle_lang.addItem("العربية", "ar")
        self.subtitle_lang.addItem("الإنجليزية", "en")
        self.subtitle_lang.setFixedWidth(110)
        self.subtitle_lang.setToolTip(
            "اللغة المختارة تُحمَّل حتى لو كانت ترجمة آلية. "
            "إن لم تتوفر، تُحمَّل اللغة الأخرى تلقائياً."
        )
        self.cookies_cb = QCheckBox("تضمين الكوكيز")

        # طبّق القيم المحفوظة قبل ربط الـ signals لتفادي إطلاقها أثناء الاستعادة
        s = self._saved_settings
        self.high_audio_choice.setChecked(bool(s.get("high_audio", False)))
        self.high_video_choice.setChecked(bool(s.get("high_video", False)))
        self.subtitle_cb.setChecked(bool(s.get("subtitle", False)))
        idx = 0 if s.get("subtitle_lang", "ar") == "ar" else 1
        self.subtitle_lang.setCurrentIndex(idx)
        self.cookies_cb.setChecked(bool(s.get("cookies", False)))

        self.high_audio_choice.stateChanged.connect(self._on_high_audio_changed)
        self.high_video_choice.stateChanged.connect(self._on_high_video_changed)
        self.subtitle_cb.stateChanged.connect(self._on_subtitle)
        self.subtitle_lang.currentIndexChanged.connect(self._on_subtitle_lang)
        self.cookies_cb.stateChanged.connect(self._on_cookies)

        opts_row.addWidget(self.high_audio_choice)
        opts_row.addWidget(self.high_video_choice)
        opts_row.addWidget(self.subtitle_cb)
        opts_row.addWidget(self.subtitle_lang)
        opts_row.addWidget(self.cookies_cb)
        opts_row.addStretch(1)

        # زر قائمة الانتظار: يلتقط أي رابط يُنسخ إلى الحافظة أثناء عمل البرنامج
        # ويحلّله في الخلفية تلقائياً، ويعرض النتائج عند الضغط عليه.
        self.queue_btn = QPushButton("🕒 قائمة الانتظار")
        self.queue_btn.setToolTip(
            "الروابط التي تنسخها أثناء استخدام البرنامج تُلتقط وتُحلَّل تلقائياً "
            "في الخلفية — اضغط لعرضها وتحميلها."
        )
        self.queue_btn.clicked.connect(self._open_queue_dialog)
        opts_row.addWidget(self.queue_btn)

        self._queue_manager = QueueManager.instance()
        self._queue_manager.item_added.connect(self._update_queue_btn)
        self._queue_manager.item_removed.connect(self._update_queue_btn)
        self._update_queue_btn()

        self.reset_btn = QPushButton("🔄")
        self.reset_btn.setFixedSize(40, 30)
        self.reset_btn.setToolTip("إعادة تعيين")
        self.reset_btn.clicked.connect(self.reset)
        opts_row.addWidget(self.reset_btn)

        root.addLayout(opts_row)

        # مسارات
        paths_row = QHBoxLayout()
        self.video_path_btn = QPushButton("🎬 مسار الفيديو")
        self.video_path_btn.clicked.connect(lambda: self._choose_path("self.path_video_btn"))
        self.audio_path_btn = QPushButton("🎧 مسار الصوت")
        self.audio_path_btn.clicked.connect(lambda: self._choose_path("self.path_audio_btn"))

        self.video_path_label = QLabel("")
        self.video_path_label.setObjectName("PathLabel")
        self.audio_path_label = QLabel("")
        self.audio_path_label.setObjectName("PathLabel")

        paths_row.addWidget(self.video_path_btn)
        paths_row.addWidget(self.video_path_label, 1)
        paths_row.addWidget(self.audio_path_btn)
        paths_row.addWidget(self.audio_path_label, 1)

        root.addLayout(paths_row)

        # تجعل النقر على الـ labels يفتح المسار
        self.video_path_label.mousePressEvent = lambda e: self._open_path(self.video_path_label.text().strip())
        self.audio_path_label.mousePressEvent = lambda e: self._open_path(self.audio_path_label.text().strip())

    def _make_quality_btn(self, text):
        b = QPushButton(text)
        b.setObjectName("QualityButton")
        b.setMinimumHeight(55)
        b.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        b.setEnabled(False)
        return b

    def _load_paths(self):
        data = load_paths()
        self.video_path_label.setText(f" {data['path_video']} ")
        self.audio_path_label.setText(f" {data['path_audio']} ")

    def _set_time(self, text):
        """ضبط ليبل الوقت overlay وإعادة موضعه في الزاوية السفلى اليمنى."""
        self.time_label.setText(text)
        self.time_label.adjustSize()
        self.time_label.move(247 - self.time_label.width() - 6,
                             117 - self.time_label.height() - 6)
        self.time_label.raise_()

    def _open_path(self, p):
        p = p.strip()
        if not p or not os.path.exists(p):
            return
        QDesktopServices.openUrl(QUrl.fromLocalFile(p))

    # --------------------------- قائمة الانتظار ----------------------------- #
    def _update_queue_btn(self, *args):
        try:
            n = self._queue_manager.count()
        except Exception:
            n = 0
        self.queue_btn.setText(f"🕒 قائمة الانتظار ({n})" if n else "🕒 قائمة الانتظار")

    def _open_queue_dialog(self):
        # النافذة تُنشأ مرة واحدة فقط وتبقى حيّة طوال عمل البرنامج (غير مودال)
        # ثم تُخفى/تُظهر فقط بعد ذلك، بدل إنشائها وتدميرها في كل ضغطة زر —
        # كان التدمير المتكرر يُعرّض ثريدات الصور المصغّرة النشطة لتدمير
        # مفاجئ يُغلق البرنامج بأكمله.
        if getattr(self, "_queue_dialog", None) is None:
            self._queue_dialog = QueueDialog(self)
        self._queue_dialog.show()
        self._queue_dialog.raise_()
        self._queue_dialog.activateWindow()

    # --------------------------- Analyze flow ------------------------------ #
    def _start_analyze(self):
        try:
            url = pyperclip.paste().split("&")[0].strip()
        except Exception:
            url = ""
        self.start_analyze_for_url(url, show_warning=True)

    def start_analyze_for_url(self, url: str, show_warning: bool = False):
        """تحليل رابط محدد مباشرة (يُستخدم أيضاً عند الرجوع من تبويب التحميل المتعدد)."""
        url = (url or "").split("&")[0].strip()
        if not _validate_url(url):
            if show_warning:
                QMessageBox.warning(self, "رابط غير صالح",
                                    "انسخ رابطاً صالحاً (http/https) ثم اضغط تحليل.")
            return False
        if not self.analyze_btn.isEnabled():
            return False
        # فيسبوك وساوندكلاود يُحلَّلان تلقائياً في شاشة "تحميل الجميع" لأنها تعرض كل التنسيقات.
        if _is_force_platform(url):
            self.request_force_analyze.emit(url)
            return True
        self.url = url
        self.reset(soft=True)
        self.analyze_btn.setEnabled(False)
        self.analyze_btn.setText("جاري التحليل...")

        # نحتفظ بكل الـ threads النشطة لمنع garbage collection قبل انتهائها
        if not hasattr(self, "_active_threads"):
            self._active_threads = []

        thread = QThread()
        worker = AnalyzeWorker(self.url, self.flag)
        worker.moveToThread(thread)
        thread.started.connect(worker.run)
        worker.finished.connect(self._on_analyze_done)
        worker.error.connect(self._on_analyze_error)
        worker.finished.connect(thread.quit)
        worker.error.connect(thread.quit)
        # احذف الـ worker والـ thread فقط بعد خروج الـ thread من event loop
        thread.finished.connect(worker.deleteLater)
        thread.finished.connect(thread.deleteLater)
        thread.finished.connect(lambda t=thread: self._cleanup_thread(t))
        self._active_threads.append((thread, worker))
        thread.start()
        return True

    def _cleanup_thread(self, thread):
        """إزالة الـ thread المنتهي من قائمة الـ threads النشطة."""
        if hasattr(self, "_active_threads"):
            self._active_threads = [
                (t, w) for (t, w) in self._active_threads if t is not thread
            ]

    def _on_analyze_done(self, result):
        self.analyze_btn.setEnabled(True)
        self.analyze_btn.setText("تحليل رابط التحميل")
        if not result:
            QMessageBox.warning(self, "خطأ", "تعذّر تحليل الرابط.")
            return
        ids, sizes, ids_h, sizes_h, info = result
        self.ids = ids
        self.sizes = sizes
        self.ids_heigh = ids_h
        self.sizes_heigh = sizes_h
        self.info_video = info

        if info and len(info) >= 3:
            self.title_label.setText(info[0] or "")
            self._set_time(info[2] or "00:00:00")
            try:
                pix = MAIN_BACKEND.picture(info[1])
                if not pix.isNull():
                    self.photo_label.setPixmap(pix.scaled(
                        self.photo_label.size(),
                        Qt.AspectRatioMode.KeepAspectRatio,
                        Qt.TransformationMode.SmoothTransformation,
                    ))
            except Exception as e:
                print(f"thumbnail error: {e}")

        self._refresh_buttons_text()

    def _on_analyze_error(self, msg):
        self.analyze_btn.setEnabled(True)
        self.analyze_btn.setText("تحليل رابط التحميل")
        QMessageBox.critical(self, "خطأ في التحليل", msg)

    # --------------------------- Buttons text ------------------------------ #
    def _refresh_buttons_text(self):
        if not self.sizes:
            return
        use_hv = self.high_video_choice.isChecked()
        use_ha = self.high_audio_choice.isChecked()
        sizes = self.sizes_heigh if use_hv else self.sizes
        if not sizes or len(sizes) < 2:
            return

        # أزرار الصوت
        if sizes[0] != '':
            self.low_audio_btn.setText(f" Audio : {sizes[0]} MB")
            self.low_audio_btn.setEnabled(True)
            self.high_audio_btn.setText(f" Audio : {sizes[1]} MB")
            self.high_audio_btn.setEnabled(True)
        else:
            self.low_audio_btn.setText(" غير متاح ")
            self.low_audio_btn.setEnabled(False)
            self.high_audio_btn.setText(" غير متاح ")
            self.high_audio_btn.setEnabled(False)

        res_names = ['144p', '240p', '360p', '480p', '720p', '1080p']
        btns = [self.b144p_btn, self.b240p_btn, self.b360p_btn,
                self.b480p_btn, self.b720p_btn, self.b1080p_btn]

        audio_size = sizes[1] if use_ha else sizes[0]
        for i, btn in enumerate(btns):
            if i + 2 >= len(sizes) or sizes[i + 2] == '':
                btn.setText(" غير متاح ")
                btn.setEnabled(False)
            else:
                total = round(sizes[i + 2] + audio_size, 2)
                btn.setText(f" {res_names[i]} : {total} MB")
                btn.setEnabled(True)

    # --------------------------- Press download ---------------------------- #
    def _press(self, key):
        if not self.ids or not self.info_video:
            return
        use_hv = self.high_video_choice.isChecked()
        ids = self.ids_heigh if use_hv else self.ids
        if not ids:
            return

        try:
            with open(PATHS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            data = load_paths()

        path_audio = data.get("path_audio", default_downloads_dir())
        path_video = data.get("path_video", default_downloads_dir())
        name = re.sub(r'[#]', '', self.info_video[0])

        # تحديد فهرس الصوت (0 منخفض، 1 عالي)
        audio_idx = 1 if self.high_audio_choice.isChecked() else 0

        # خريطة فهارس الأزرار في ids
        # ids[0]=audio_low, ids[1]=audio_high, ids[2..7]=144..1080
        if key == "low_audio":
            fmt = ids[0]
            out = os.path.join(path_audio, f"{name}.mp3")
        elif key == "high_audio":
            fmt = ids[1]
            out = os.path.join(path_audio, f"{name}.mp3")
        else:
            res_to_idx = {"144p": 2, "240p": 3, "360p": 4, "480p": 5, "720p": 6, "1080p": 7}
            vi = res_to_idx[key]
            if not ids[vi]:
                QMessageBox.warning(self, "غير متاح", "هذه الجودة غير متاحة.")
                return
            fmt = f"{ids[audio_idx]}+{ids[vi]}"
            out = os.path.join(path_video, name)

        # علِّم الزر بنجاح الإرسال
        btn = self.quality_buttons.get(key)
        if btn:
            btn.setObjectName("QualityActive")
            btn.setStyle(btn.style())  # إعادة تطبيق
            btn.style().unpolish(btn); btn.style().polish(btn)

        # أنشئ مهمة وأرسلها للمدير
        task_flag = dict(self.flag)
        task = DownloadTask(
            url=self.url,
            format_id=fmt,
            output_path=out,
            flag=task_flag,
            display_name=os.path.basename(out) or name,
            thumbnail_url=self.info_video[1] if len(self.info_video) > 1 else "",
        )
        DownloadManager.instance().add_task(task)

    # --------------------------- choose path ------------------------------- #
    def _choose_path(self, key):
        path = QFileDialog.getExistingDirectory(self, "اختر مجلداً")
        if not path:
            return
        data = MAIN_BACKEND.choice_path_back(key, path)
        self.video_path_label.setText(f" {data.get('path_video', '')} ")
        self.audio_path_label.setText(f" {data.get('path_audio', '')} ")

    # --------------------------- options ---------------------------------- #
    def _on_subtitle(self, state):
        self.flag["subtitle"] = bool(state)
        if "subtitle_lang" not in self.flag:
            self.flag["subtitle_lang"] = self.subtitle_lang.currentData() or "ar"
        update_value("main", "subtitle", bool(state))

    def _on_subtitle_lang(self, idx):
        lang = self.subtitle_lang.currentData() or "ar"
        self.flag["subtitle_lang"] = lang
        update_value("main", "subtitle_lang", lang)

    def _on_cookies(self, state):
        self.flag["op"] = bool(state)
        update_value("main", "cookies", bool(state))

    def _on_high_audio_changed(self, state):
        update_value("main", "high_audio", bool(state))
        self._refresh_buttons_text()

    def _on_high_video_changed(self, state):
        update_value("main", "high_video", bool(state))
        self._refresh_buttons_text()

    # --------------------------- reset ------------------------------------ #
    def reset(self, soft=False):
        # soft=True: لا نمسح خانات الاختيار
        self.title_label.setText(" سُبْحَانَ اللَّهِ وَبِحَمْدِهِ، سُبْحَانَ اللَّهِ الْعَظِيمِ")
        self._set_time("00:00:00")
        self.photo_label.clear()
        self.photo_label.setStyleSheet("background-color: silver; border-radius: 10px;")

        for b in self.quality_buttons.values():
            b.setEnabled(False)
            b.setObjectName("QualityButton")
            b.style().unpolish(b); b.style().polish(b)

        self.low_audio_btn.setText(" Audio : ")
        self.high_audio_btn.setText(" Audio : ")
        for txt, b in zip(
            [" 144p : ", " 240p : ", " 360p : ", " 480p : ", " 720p : ", " 1080p : "],
            [self.b144p_btn, self.b240p_btn, self.b360p_btn,
             self.b480p_btn, self.b720p_btn, self.b1080p_btn],
        ):
            b.setText(txt)

        if not soft:
            self.high_audio_choice.setChecked(False)
            self.high_video_choice.setChecked(False)
            self.subtitle_cb.setChecked(False)

        self.ids = []
        self.sizes = []
        self.ids_heigh = []
        self.sizes_heigh = []
        self.info_video = []


FORCE_BACKEND = YouTubeDownloader()


def _validate_url(u):
    return _is_valid_url(u)


class FetchWorker(QObject):
    finished = pyqtSignal(object)  # (audio, video, video_audio, info_url)
    error = pyqtSignal(str)

    def __init__(self, url, flag):
        super().__init__()
        self.url = url
        self.flag = flag

    def run(self):
        try:
            r = FORCE_BACKEND.information_force(self.url, self.flag)
            self.finished.emit(r)
        except Exception as e:
            self.error.emit(str(e))


class ForceTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        s = get_section("force")
        self.flag = {
            "op": bool(s.get("cookies", False)),
            "subtitle": bool(s.get("subtitle", False)),
            "subtitle_lang": s.get("subtitle_lang", "ar"),
        }
        self._saved_settings = s
        self.url = ""
        self.audio = {}
        self.video = {}
        self.video_audio = {}
        self.info_url = []

        self.audio_checks = []
        self.video_checks = []
        self.av_checks = []
        self.selected_audio_idx = None
        self.selected_video_idx = None
        self.selected_av_idx = None

        self._build_ui()
        self._load_paths()

    def _build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(12, 12, 12, 12)
        root.setSpacing(8)

        # شريط علوي بزرين
        top = QHBoxLayout()
        self.analyze_btn = QPushButton("تحليل رابط التحميل")
        self.analyze_btn.setObjectName("PrimaryButton")
        self.analyze_btn.setMinimumHeight(56)
        self.analyze_btn.clicked.connect(self._start_fetch)
        top.addWidget(self.analyze_btn, 1)

        self.download_btn = QPushButton("اختر تنسيقاً للتحميل")
        self.download_btn.setObjectName("PrimaryButton")
        self.download_btn.setMinimumHeight(56)
        self.download_btn.setEnabled(False)
        self.download_btn.clicked.connect(self._press_download)
        top.addWidget(self.download_btn, 1)
        root.addLayout(top)

        # ثلاث قوائم تمرير جنباً إلى جنب
        lists_row = QHBoxLayout()

        self.av_panel, self.av_inner_layout = self._make_panel("التنسيقات المدمجة")
        self.video_panel, self.video_inner_layout = self._make_panel("تنسيقات الفيديو")
        self.audio_panel, self.audio_inner_layout = self._make_panel("تنسيقات الصوت")

        lists_row.addWidget(self.av_panel, 1)
        lists_row.addWidget(self.video_panel, 1)
        lists_row.addWidget(self.audio_panel, 1)
        root.addLayout(lists_row, 1)

        # معلومات الفيديو - العنوان والصورة محاذيان (الوقت overlay)
        info_row = QHBoxLayout()
        info_row.setContentsMargins(0, 0, 0, 0)
        self.title_label = QLabel(" سُبْحَانَ اللَّهِ وَبِحَمْدِهِ، سُبْحَانَ اللَّهِ الْعَظِيمِ")
        self.title_label.setObjectName("TitleLabel")
        self.title_label.setWordWrap(True)
        self.title_label.setFixedHeight(117)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        info_row.addWidget(self.title_label, 3)

        self.photo_container = QWidget()
        self.photo_container.setFixedSize(247, 117)
        self.photo_label = QLabel(self.photo_container)
        self.photo_label.setGeometry(0, 0, 247, 117)
        self.photo_label.setStyleSheet("background-color: silver; border-radius: 10px;")
        self.photo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.time_label = QLabel("00:00:00", self.photo_container)
        self.time_label.setStyleSheet(
            "background-color: rgba(0, 0, 0, 180);"
            "color: white;"
            "font-weight: bold;"
            "font-size: 14px;"
            "padding: 2px 6px;"
            "border-radius: 4px;"
        )
        self.time_label.adjustSize()
        self.time_label.move(247 - self.time_label.width() - 6,
                             117 - self.time_label.height() - 6)
        self.time_label.raise_()

        info_row.addWidget(self.photo_container, 0, Qt.AlignmentFlag.AlignVCenter)
        root.addLayout(info_row)

        # خيارات + مسارات
        opts = QHBoxLayout()
        self.subtitle_cb = QCheckBox("إضافة الترجمة")
        self.subtitle_lang = QComboBox()
        self.subtitle_lang.addItem("العربية", "ar")
        self.subtitle_lang.addItem("الإنجليزية", "en")
        self.subtitle_lang.setFixedWidth(110)
        self.cookies_cb = QCheckBox("تضمين الكوكيز")
        # طبّق المحفوظات قبل ربط الإشارات
        ss = self._saved_settings
        self.subtitle_cb.setChecked(bool(ss.get("subtitle", False)))
        self.subtitle_lang.setCurrentIndex(0 if ss.get("subtitle_lang", "ar") == "ar" else 1)
        self.cookies_cb.setChecked(bool(ss.get("cookies", False)))

        def _on_sub(state):
            self.flag["subtitle"] = bool(state)
            update_value("force", "subtitle", bool(state))
        def _on_sub_lang(i):
            lang = self.subtitle_lang.currentData() or "ar"
            self.flag["subtitle_lang"] = lang
            update_value("force", "subtitle_lang", lang)
        def _on_ck(state):
            self.flag["op"] = bool(state)
            update_value("force", "cookies", bool(state))

        self.subtitle_cb.stateChanged.connect(_on_sub)
        self.subtitle_lang.currentIndexChanged.connect(_on_sub_lang)
        self.cookies_cb.stateChanged.connect(_on_ck)
        opts.addWidget(self.subtitle_cb)
        opts.addWidget(self.subtitle_lang)
        opts.addWidget(self.cookies_cb)
        opts.addStretch(1)

        self.reset_btn = QPushButton("🔄")
        self.reset_btn.setFixedSize(40, 30)
        self.reset_btn.clicked.connect(self.reset)
        opts.addWidget(self.reset_btn)
        root.addLayout(opts)

        paths = QHBoxLayout()
        self.video_path_btn = QPushButton("🎬 مسار الفيديو")
        self.video_path_btn.clicked.connect(lambda: self._choose_path("self.path_video_btn"))
        self.audio_path_btn = QPushButton("🎧 مسار الصوت")
        self.audio_path_btn.clicked.connect(lambda: self._choose_path("self.path_audio_btn"))
        self.video_path_label = QLabel("")
        self.video_path_label.setObjectName("PathLabel")
        self.audio_path_label = QLabel("")
        self.audio_path_label.setObjectName("PathLabel")
        paths.addWidget(self.video_path_btn)
        paths.addWidget(self.video_path_label, 1)
        paths.addWidget(self.audio_path_btn)
        paths.addWidget(self.audio_path_label, 1)
        root.addLayout(paths)

        self.video_path_label.mousePressEvent = lambda e: self._open_path(self.video_path_label.text().strip())
        self.audio_path_label.mousePressEvent = lambda e: self._open_path(self.audio_path_label.text().strip())

    def _make_panel(self, title):
        frame = QFrame()
        frame.setObjectName("Panel")
        v = QVBoxLayout(frame)
        v.setContentsMargins(6, 6, 6, 6)
        v.setSpacing(4)
        lbl = QLabel(title)
        lbl.setStyleSheet("font-size: 20px; font-weight: bold;")
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        v.addWidget(lbl)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content = QWidget()
        inner = QVBoxLayout(content)
        inner.setSpacing(4)
        inner.addStretch(1)
        scroll.setWidget(content)
        v.addWidget(scroll, 1)
        return frame, inner

    def _load_paths(self):
        d = load_paths()
        self.video_path_label.setText(f" {d['path_video']} ")
        self.audio_path_label.setText(f" {d['path_audio']} ")

    def _set_time(self, text):
        self.time_label.setText(text)
        self.time_label.adjustSize()
        self.time_label.move(247 - self.time_label.width() - 6,
                             117 - self.time_label.height() - 6)
        self.time_label.raise_()

    def _open_path(self, p):
        p = p.strip()
        if p and os.path.exists(p):
            QDesktopServices.openUrl(QUrl.fromLocalFile(p))

    # --------------------------- fetch ------------------------------------ #
    def _start_fetch(self):
        try:
            url = pyperclip.paste().split("&")[0].strip()
        except Exception:
            url = ""
        self.start_fetch_for_url(url)

    def start_fetch_for_url(self, url: str):
        """بدء تحليل مباشر لرابط محدد (يُستخدم عند التحويل من الرئيسية)."""
        url = (url or "").split("&")[0].strip()
        if not _validate_url(url):
            QMessageBox.warning(self, "رابط غير صالح", "انسخ رابطاً صالحاً ثم اضغط تحليل.")
            return
        self.url = url
        self.reset(soft=True)
        self.analyze_btn.setEnabled(False)
        self.analyze_btn.setText("جاري التحليل...")

        if not hasattr(self, "_active_threads"):
            self._active_threads = []

        thread = QThread()
        worker = FetchWorker(self.url, self.flag)
        worker.moveToThread(thread)
        thread.started.connect(worker.run)
        worker.finished.connect(self._on_fetched)
        worker.error.connect(self._on_error)
        worker.finished.connect(thread.quit)
        worker.error.connect(thread.quit)
        thread.finished.connect(worker.deleteLater)
        thread.finished.connect(thread.deleteLater)
        thread.finished.connect(lambda t=thread: self._cleanup_thread(t))
        self._active_threads.append((thread, worker))
        thread.start()
        return True

    def _cleanup_thread(self, thread):
        if hasattr(self, "_active_threads"):
            self._active_threads = [
                (t, w) for (t, w) in self._active_threads if t is not thread
            ]

    def _on_error(self, msg):
        self.analyze_btn.setEnabled(True)
        self.analyze_btn.setText("تحليل رابط التحميل")
        QMessageBox.critical(self, "خطأ", msg)

    def _on_fetched(self, result):
        self.analyze_btn.setEnabled(True)
        self.analyze_btn.setText("تحليل رابط التحميل")
        if not result:
            return
        self.audio, self.video, self.video_audio, self.info_url = result

        # تعبئة الواجهة
        if self.info_url:
            self.title_label.setText(self.info_url[0] or "")
            t = self.info_url[1] or 0
            self._set_time(f"{t // 3600:02}:{(t % 3600) // 60:02}:{t % 60:02}")
            try:
                pix = FORCE_BACKEND.picture(self.info_url[2])
                if not pix.isNull():
                    self.photo_label.setPixmap(pix.scaled(
                        self.photo_label.size(),
                        Qt.AspectRatioMode.KeepAspectRatio,
                        Qt.TransformationMode.SmoothTransformation,
                    ))
            except Exception as e:
                print(f"thumb error: {e}")

        # ملء القوائم - مع دعم القيم النصية لـ HD/SD (فيسبوك)
        def _combined_label(i):
            v0 = self.video_audio[i][0]
            sz = self.video_audio[i][2]
            # لو القيمة نصية (HD/SD من فيسبوك) نعرضها كما هي
            if isinstance(v0, str):
                return f"{v0} : {sz} MB"
            return f"{v0 or '-'}p : {sz} MB"

        def _video_label(i):
            v0 = self.video[i][0]
            sz = self.video[i][2]
            if isinstance(v0, str):
                return f"{v0} : {sz} MB"
            return f"{v0 or '-'}p : {sz} MB"

        def _audio_label(i):
            abr = self.audio[i][0]
            sz = self.audio[i][2]
            try:
                abr_int = int(float(abr or 0))
            except (TypeError, ValueError):
                abr_int = 0
            if abr_int <= 0:
                return f"Audio : {sz} MB"
            return f"Audio {abr_int}kp : {sz} MB"

        # لفيسبوك: تأكيد ظهور SD و HD دائماً في التنسيقات المدمجة، ويفضّل عرضهما أولاً.
        if _is_facebook_url(self.url) and self.video_audio:
            ordered = {}
            special = []
            normal = []
            for k, v in self.video_audio.items():
                label = str(v[0]).strip().lower()
                fid = str(v[1]).strip().lower()
                (special if label in ("sd", "hd") or fid in ("sd", "hd") else normal).append((k, v))
            for _, v in sorted(special, key=lambda kv: 0 if str(kv[1][1]).lower() == "sd" else 1):
                ordered[len(ordered)] = v
            for _, v in normal:
                ordered[len(ordered)] = v
            self.video_audio = ordered

        self._fill_list(self.av_inner_layout, self.video_audio,
                        _combined_label, self.av_checks, self._select_av)
        self._fill_list(self.video_inner_layout, self.video,
                        _video_label, self.video_checks, self._select_video)
        self._fill_list(self.audio_inner_layout, self.audio,
                        _audio_label, self.audio_checks, self._select_audio)

    def _fill_list(self, layout, items, label_fn, target_list, on_select):
        # امسح القائمة (ما عدا stretch)
        for cb in target_list:
            cb.setParent(None)
            cb.deleteLater()
        target_list.clear()
        # احذف stretch القديم
        while layout.count():
            it = layout.takeAt(0)
            w = it.widget()
            if w is not None:
                w.setParent(None)
                w.deleteLater()
        # أضف عناصر
        for i in range(len(items)):
            cb = QCheckBox(label_fn(i))
            cb.stateChanged.connect(lambda s, idx=i: on_select(idx, s))
            layout.addWidget(cb)
            target_list.append(cb)
        layout.addStretch(1)

    # --------------------------- selection -------------------------------- #
    def _select_audio(self, index, state):
        if state:
            for i, cb in enumerate(self.audio_checks):
                if i != index:
                    cb.blockSignals(True); cb.setChecked(False); cb.blockSignals(False)
            for cb in self.av_checks:
                cb.blockSignals(True); cb.setChecked(False); cb.blockSignals(False)
            self.selected_audio_idx = index
            self.selected_av_idx = None
        else:
            self.selected_audio_idx = None
        self._update_download_btn()

    def _select_video(self, index, state):
        if state:
            for i, cb in enumerate(self.video_checks):
                if i != index:
                    cb.blockSignals(True); cb.setChecked(False); cb.blockSignals(False)
            for cb in self.av_checks:
                cb.blockSignals(True); cb.setChecked(False); cb.blockSignals(False)
            self.selected_video_idx = index
            self.selected_av_idx = None
        else:
            self.selected_video_idx = None
        self._update_download_btn()

    def _select_av(self, index, state):
        if state:
            for i, cb in enumerate(self.av_checks):
                if i != index:
                    cb.blockSignals(True); cb.setChecked(False); cb.blockSignals(False)
            for cb in self.audio_checks:
                cb.blockSignals(True); cb.setChecked(False); cb.blockSignals(False)
            for cb in self.video_checks:
                cb.blockSignals(True); cb.setChecked(False); cb.blockSignals(False)
            self.selected_av_idx = index
            self.selected_audio_idx = None
            self.selected_video_idx = None
        else:
            self.selected_av_idx = None
        self._update_download_btn()

    def _compute_id_and_size(self):
        ai = self.selected_audio_idx
        vi = self.selected_video_idx
        avi = self.selected_av_idx
        fmt = ""
        size = 0
        if ai is not None and vi is None and avi is None:
            fmt = str(self.audio[ai][1])
            size = self.audio[ai][2]
        elif ai is None and vi is not None and avi is None:
            fmt = str(self.video[vi][1])
            size = self.video[vi][2]
        elif ai is not None and vi is not None:
            fmt = f"{self.audio[ai][1]}+{self.video[vi][1]}"
            size = self.audio[ai][2] + self.video[vi][2]
        elif avi is not None:
            fmt = str(self.video_audio[avi][1])
            size = self.video_audio[avi][2]
        return fmt, size

    def _update_download_btn(self):
        fmt, size = self._compute_id_and_size()
        if not fmt:
            self.download_btn.setText("اختر تنسيقاً للتحميل")
            self.download_btn.setEnabled(False)
        else:
            self.download_btn.setText(f"تحميل  -  {round(size, 2)} MB")
            self.download_btn.setEnabled(True)

    # --------------------------- download --------------------------------- #
    def _press_download(self):
        if not self.info_url:
            return
        try:
            with open(PATHS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            data = load_paths()
        path_audio = data.get("path_audio", default_downloads_dir())
        path_video = data.get("path_video", default_downloads_dir())

        fmt, size = self._compute_id_and_size()
        if not fmt:
            return
        name = FORCE_BACKEND.clean_filename(self.info_url[0] or "untitled")

        # تحديد المسار النهائي
        if self.selected_audio_idx is not None and self.selected_video_idx is None and self.selected_av_idx is None:
            out = os.path.join(path_audio, f"{name}.mp3")
        elif _is_facebook_url(self.url):
            # فيديوهات Facebook دائماً mp4 وباسم مؤرخ لتفادي تعارض أسماء
            # عدة فيديوهات مصدرها الصفحة نفسها.
            out = _facebook_video_output_path(path_video, name, ".mp4")
        elif self.selected_av_idx is not None:
            out = os.path.join(path_video, f"{name}.mp4")
        else:
            out = os.path.join(path_video, name)

        task = DownloadTask(
            url=self.url,
            format_id=fmt,
            output_path=out,
            flag=dict(self.flag),
            display_name=os.path.basename(out) or name,
            thumbnail_url=self.info_url[2] if len(self.info_url) > 2 else "",
        )
        DownloadManager.instance().add_task(task)

    def _choose_path(self, key):
        path = QFileDialog.getExistingDirectory(self, "اختر مجلداً")
        if not path:
            return
        data = FORCE_BACKEND.choice_path_back(key, path)
        self.video_path_label.setText(f" {data.get('path_video', '')} ")
        self.audio_path_label.setText(f" {data.get('path_audio', '')} ")

    # --------------------------- reset ------------------------------------ #
    def reset(self, soft=False):
        # امسح القوائم
        for layout, lst in [
            (self.audio_inner_layout, self.audio_checks),
            (self.video_inner_layout, self.video_checks),
            (self.av_inner_layout, self.av_checks),
        ]:
            for cb in lst:
                cb.setParent(None); cb.deleteLater()
            lst.clear()
            while layout.count():
                it = layout.takeAt(0)
                w = it.widget()
                if w is not None:
                    w.setParent(None); w.deleteLater()
            layout.addStretch(1)

        self.selected_audio_idx = None
        self.selected_video_idx = None
        self.selected_av_idx = None
        self.download_btn.setEnabled(False)
        self.download_btn.setText("اختر تنسيقاً للتحميل")

        if not soft:
            self.title_label.setText(" سُبْحَانَ اللَّهِ وَبِحَمْدِهِ، سُبْحَانَ اللَّهِ الْعَظِيمِ")
            self._set_time("00:00:00")
            self.photo_label.clear()
            self.photo_label.setStyleSheet("background-color: silver; border-radius: 10px;")
            self.subtitle_cb.setChecked(False)
            self.cookies_cb.setChecked(False)


_RES = ['Audio', 'Audio', '144p', '240p', '360p', '480p', '720p', '1080p']


class FetchPlaylistWorker(QObject):
    finished = pyqtSignal(object, object)  # (links, title)
    error = pyqtSignal(str)

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        try:
            opts = {
                'quiet': True,
                'extract_flat': True,
                'force_generic_extractor': False,
                'no_warnings': True,
            }
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(self.url, download=False) or {}
            if 'entries' in info:
                links = [e['url'] for e in info['entries'] if e and e.get('url')]
                title = info.get('title', 'Playlist')
                self.finished.emit(links, title)
            else:
                self.error.emit("لم يتم العثور على قائمة تشغيل.")
        except Exception as e:
            self.error.emit(str(e))


class AnalyzeRangeWorker(QObject):
    item_done = pyqtSignal(int, object)  # i, dict-data
    finished = pyqtSignal()
    error = pyqtSignal(str)

    def __init__(self, links, start, end, flag):
        super().__init__()
        self.links = links
        self.start = start
        self.end = end
        self.flag = flag
        self._cancel = False

    def cancel(self):
        self._cancel = True

    def run(self):
        try:
            bk = YouTubeDownloader()
            for i in range(self.start, self.end):
                if self._cancel:
                    break
                link = self.links[i]
                try:
                    low_id, low_sz, hi_id, hi_sz, info = bk.fun_for_all(link, self.flag)
                except Exception as ie:
                    print(f"[list] خطأ تحليل {link}: {ie}")
                    continue
                self.item_done.emit(i, {
                    'low_id': low_id, 'low_size': low_sz,
                    'heigh_id': hi_id, 'heigh_size': hi_sz,
                    'info_process': info, 'url': link,
                })
            self.finished.emit()
        except Exception as e:
            self.error.emit(str(e))


class ListTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        s = get_section("list")
        self.flag = {
            "op": bool(s.get("cookies", False)),
            "subtitle": bool(s.get("subtitle", False)),
            "subtitle_lang": s.get("subtitle_lang", "ar"),
        }
        self._saved_settings = s
        self.url = ""
        self.links = []
        self.playlist_title = ""
        self.dict_all = {}     # i -> data
        self.row_widgets = {}  # i -> [checkboxes per quality]
        self.selected_options = {}  # i -> selected res index

        self._build_ui()
        self._load_paths()

    # ------------------------------- UI ---------------------------------- #
    def _build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(10, 10, 10, 10)
        root.setSpacing(8)

        # شريط الأزرار العلوي
        top = QHBoxLayout()
        self.download_btn = QPushButton("تحميل")
        self.download_btn.setObjectName("PrimaryButton")
        self.download_btn.setEnabled(False)
        self.download_btn.clicked.connect(self._press_download)

        self.size_btn = QPushButton("حجم المحدد")
        self.size_btn.setObjectName("PrimaryButton")

        self.start_combo = QComboBox()
        self.start_combo.addItem("بداية")
        self.end_combo = QComboBox()
        self.end_combo.addItem("نهاية")

        self.analyze_btn = QPushButton("تحليل النطاق")
        self.analyze_btn.setObjectName("PrimaryButton")
        self.analyze_btn.setEnabled(False)
        self.analyze_btn.clicked.connect(self._start_analyze_range)

        self.pick_btn = QPushButton("نسخ الرابط")
        self.pick_btn.setObjectName("PrimaryButton")
        self.pick_btn.clicked.connect(self._pick_link)

        self.reset_btn = QPushButton("🔄 ريسيت")
        self.reset_btn.setToolTip("مسح كل الفيديوهات والاختيارات")
        self.reset_btn.clicked.connect(self.reset)

        top.addWidget(self.download_btn)
        top.addWidget(self.size_btn)
        top.addWidget(QLabel("بداية:"))
        top.addWidget(self.start_combo)
        top.addWidget(QLabel("نهاية:"))
        top.addWidget(self.end_combo)
        top.addWidget(self.analyze_btn)
        top.addWidget(self.pick_btn)
        top.addWidget(self.reset_btn)
        root.addLayout(top)

        # صف تحديد الكل / إلغاء الكل لجودة معينة
        bulk = QHBoxLayout()
        bulk.addWidget(QLabel("تطبيق على الكل لجودة:"))
        self.bulk_quality = QComboBox()
        self.bulk_quality.addItems(_RES[2:])  # الجودات المرئية فقط
        self.bulk_quality.insertItem(0, "Audio (منخفض)")
        self.bulk_quality.insertItem(1, "Audio (عالي)")
        bulk.addWidget(self.bulk_quality)

        self.select_all_btn = QPushButton("✔ تحديد الكل")
        self.select_all_btn.clicked.connect(lambda: self._bulk_select(True))
        self.deselect_all_btn = QPushButton("✖ إلغاء الكل")
        self.deselect_all_btn.clicked.connect(lambda: self._bulk_select(False))
        bulk.addWidget(self.select_all_btn)
        bulk.addWidget(self.deselect_all_btn)
        bulk.addStretch(1)
        root.addLayout(bulk)

        # خيارات
        opts = QHBoxLayout()
        self.high_audio_cb = QCheckBox("صوت فائق الجودة")
        self.high_video_cb = QCheckBox("فيديو فائق الجودة")
        self.subtitle_cb = QCheckBox("إضافة الترجمة")
        self.subtitle_lang = QComboBox()
        self.subtitle_lang.addItem("العربية", "ar")
        self.subtitle_lang.addItem("الإنجليزية", "en")
        self.subtitle_lang.setFixedWidth(110)
        self.cookies_cb = QCheckBox("تضمين الكوكيز")
        # طبّق المحفوظات
        ss = self._saved_settings
        self.high_audio_cb.setChecked(bool(ss.get("high_audio", False)))
        self.high_video_cb.setChecked(bool(ss.get("high_video", False)))
        self.subtitle_cb.setChecked(bool(ss.get("subtitle", False)))
        self.subtitle_lang.setCurrentIndex(0 if ss.get("subtitle_lang", "ar") == "ar" else 1)
        self.cookies_cb.setChecked(bool(ss.get("cookies", False)))

        def _on_ha(s):
            update_value("list", "high_audio", bool(s))
            self._refresh_labels()
        def _on_hv(s):
            update_value("list", "high_video", bool(s))
            self._refresh_labels()
        def _on_sub(s):
            self.flag["subtitle"] = bool(s)
            update_value("list", "subtitle", bool(s))
        def _on_sub_lang(i):
            lang = self.subtitle_lang.currentData() or "ar"
            self.flag["subtitle_lang"] = lang
            update_value("list", "subtitle_lang", lang)
        def _on_ck(s):
            self.flag["op"] = bool(s)
            update_value("list", "cookies", bool(s))

        self.high_audio_cb.stateChanged.connect(_on_ha)
        self.high_video_cb.stateChanged.connect(_on_hv)
        self.subtitle_cb.stateChanged.connect(_on_sub)
        self.subtitle_lang.currentIndexChanged.connect(_on_sub_lang)
        self.cookies_cb.stateChanged.connect(_on_ck)
        opts.addWidget(self.high_audio_cb)
        opts.addWidget(self.high_video_cb)
        opts.addWidget(self.subtitle_cb)
        opts.addWidget(self.subtitle_lang)
        opts.addWidget(self.cookies_cb)
        opts.addStretch(1)
        root.addLayout(opts)

        # المنطقة القابلة للتمرير لعرض الفيديوهات
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        # نمنع شريط التمرير الأفقي — كل العناصر في 4 أعمدة فقط
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_content = QWidget()
        self.grid = QGridLayout(self.scroll_content)
        self.grid.setSpacing(6)
        self.grid.setContentsMargins(6, 6, 6, 6)
        # وزّع الأعمدة الأربعة بالتساوي
        for col in range(4):
            self.grid.setColumnStretch(col, 1)
        self.scroll.setWidget(self.scroll_content)
        root.addWidget(self.scroll, 1)

        # المسارات
        paths = QHBoxLayout()
        self.path_btn = QPushButton("🎧 مسار القائمة")
        self.path_btn.clicked.connect(lambda: self._choose_path("self.path_list_btn"))
        self.path_label = QLabel("")
        self.path_label.setObjectName("PathLabel")
        self.path_label.mousePressEvent = lambda e: self._open_path(self.path_label.text().strip())
        paths.addWidget(self.path_btn)
        paths.addWidget(self.path_label, 1)
        root.addLayout(paths)

    def _load_paths(self):
        d = load_paths()
        self.path_list = d['path_list']
        self.path_label.setText(f" {self.path_list} ")

    def _open_path(self, p):
        p = p.strip()
        if p and os.path.exists(p):
            QDesktopServices.openUrl(QUrl.fromLocalFile(p))

    def _choose_path(self, key):
        path = QFileDialog.getExistingDirectory(self, "اختر مجلداً")
        if not path:
            return
        bk = YouTubeDownloader()
        d = bk.choice_path_back(key, path)
        self.path_list = d.get('path_list', path)
        self.path_label.setText(f" {self.path_list} ")

    # ------------------------------- pick playlist ------------------------ #
    def _pick_link(self):
        try:
            url = pyperclip.paste().split("&")[0].strip()
        except Exception:
            url = ""
        if not (url.startswith("http://") or url.startswith("https://")):
            QMessageBox.warning(self, "رابط غير صالح", "انسخ رابطاً صالحاً ثم اضغط نسخ الرابط.")
            return
        self.url = url
        self._reset_grid()

        # كاش
        try:
            name_json = url.split('=')[-1]
        except Exception:
            name_json = "playlist"
        cache_path = os.path.join(CACHE_INFO_DIR, f"{name_json}.json")
        if os.path.exists(cache_path):
            with open(cache_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.links = data.get("links", []) or []
            self.playlist_title = data.get("title", "Playlist")
            self._after_links_loaded()
            return

        self.pick_btn.setEnabled(False)
        self.pick_btn.setText("جاري الاستخراج...")
        if not hasattr(self, "_active_threads"):
            self._active_threads = []
        thread = QThread()
        worker = FetchPlaylistWorker(self.url)
        worker.moveToThread(thread)
        thread.started.connect(worker.run)
        worker.finished.connect(self._on_playlist_done)
        worker.error.connect(self._on_playlist_error)
        worker.finished.connect(thread.quit)
        worker.error.connect(thread.quit)
        thread.finished.connect(worker.deleteLater)
        thread.finished.connect(thread.deleteLater)
        thread.finished.connect(lambda t=thread: self._cleanup_thread(t))
        self._active_threads.append((thread, worker))
        thread.start()

    def _on_playlist_done(self, links, title):
        self.pick_btn.setEnabled(True); self.pick_btn.setText("نسخ الرابط")
        self.links = links or []
        self.playlist_title = title or "Playlist"
        # حفظ كاش
        try:
            name_json = self.url.split('=')[-1]
            cache_path = os.path.join(CACHE_INFO_DIR, f"{name_json}.json")
            os.makedirs(os.path.dirname(cache_path), exist_ok=True)
            with open(cache_path, "w", encoding="utf-8") as f:
                json.dump({"links": self.links, "title": self.playlist_title}, f,
                          indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"cache write error: {e}")
        self._after_links_loaded()

    def _on_playlist_error(self, msg):
        self.pick_btn.setEnabled(True); self.pick_btn.setText("نسخ الرابط")
        QMessageBox.critical(self, "خطأ", msg)

    def _after_links_loaded(self):
        n = len(self.links)
        self.start_combo.clear()
        self.end_combo.clear()
        self.start_combo.addItems([str(i + 1) for i in range(n)])
        self.end_combo.addItems([str(i + 1) for i in range(n)])
        if n:
            self.start_combo.setCurrentIndex(0)
            self.end_combo.setCurrentIndex(n - 1)
            self.analyze_btn.setEnabled(True)
        QMessageBox.information(self, "تم", f"عدد الفيديوهات: {n}")

    # ------------------------------- analyze range ------------------------ #
    def _start_analyze_range(self):
        if not self.links:
            return
        try:
            start = int(self.start_combo.currentText()) - 1
            end = int(self.end_combo.currentText())
        except Exception:
            QMessageBox.warning(self, "نطاق غير صالح", "اختر بداية ونهاية صحيحتين.")
            return
        if start < 0 or end > len(self.links) or start >= end:
            QMessageBox.warning(self, "نطاق غير صالح", "النطاق غير منطقي.")
            return

        self._reset_grid()
        self.analyze_btn.setEnabled(False)
        self.analyze_btn.setText("جاري التحليل...")

        if not hasattr(self, "_active_threads"):
            self._active_threads = []
        thread = QThread()
        worker = AnalyzeRangeWorker(self.links, start, end, dict(self.flag))
        worker.moveToThread(thread)
        thread.started.connect(worker.run)
        worker.item_done.connect(self._add_video_row)
        worker.finished.connect(self._on_range_done)
        worker.error.connect(self._on_range_error)
        worker.finished.connect(thread.quit)
        worker.error.connect(thread.quit)
        thread.finished.connect(worker.deleteLater)
        thread.finished.connect(thread.deleteLater)
        thread.finished.connect(lambda t=thread: self._cleanup_thread(t))
        self._active_threads.append((thread, worker))
        thread.start()
        return True

    def _cleanup_thread(self, thread):
        if hasattr(self, "_active_threads"):
            self._active_threads = [
                (t, w) for (t, w) in self._active_threads if t is not thread
            ]

    def _on_range_done(self):
        self.analyze_btn.setEnabled(True)
        self.analyze_btn.setText("تحليل النطاق")

    def _on_range_error(self, msg):
        self.analyze_btn.setEnabled(True)
        self.analyze_btn.setText("تحليل النطاق")
        QMessageBox.critical(self, "خطأ", msg)

    def _add_video_row(self, i, data):
        self.dict_all[i] = data
        info = data['info_process']
        # عنوان الفيديو
        row = self.grid.rowCount()
        title_lbl = QLabel(f"({len(self.dict_all)}) - {info[0] if info else 'video'}")
        title_lbl.setStyleSheet("font-size: 20px; font-weight: bold; color: #cfcfcf; padding: 4px;")
        # العرض الكلي = 4 أعمدة فقط (لا حاجة لشريط تمرير عرضي)
        self.grid.addWidget(title_lbl, row, 0, 1, 4)
        row += 1

        # 8 مربعات اختيار موزعة على صفّين × 4 أعمدة:
        #   الصف الأول:  Audio منخفض - Audio عالي - 144p - 240p
        #   الصف الثاني: 360p - 480p - 720p - 1080p
        checks = []
        low_size = data['low_size']
        for j in range(8):
            if j < len(low_size) and low_size[j] not in ("", None):
                if j < 2:
                    txt = f"{_RES[j]} : {round(low_size[j], 2)} MB"
                else:
                    audio0 = low_size[0] if low_size and low_size[0] not in ("", None) else 0
                    txt = f"{_RES[j]} : {round(low_size[j] + audio0, 2)} MB"
                cb = QCheckBox(txt)
                cb.setEnabled(True)
            else:
                cb = QCheckBox(f"{_RES[j]} : ❌")
                cb.setEnabled(False)
            # لون داكن متناوب بحسب العمود ضمن الصف
            col_in_row = j % 4
            color = COLOR_ALT_A if (col_in_row % 2 == 0) else COLOR_ALT_B
            cb.setStyleSheet(
                f"QCheckBox {{ background-color: {color}; padding: 6px 10px; "
                f"border-radius: 4px; font-weight: bold; }}"
            )
            cb.stateChanged.connect(
                lambda s, vi=i, ji=j: self._on_check(vi, ji, s)
            )
            # j=0..3 في الصف الأول، j=4..7 في الصف الثاني
            grid_row = row + (j // 4)
            grid_col = j % 4
            self.grid.addWidget(cb, grid_row, grid_col)
            checks.append(cb)
        self.row_widgets[i] = checks
        row += 2  # تخطّينا صفّين

        # خط فاصل
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setStyleSheet("background-color: #555;")
        line.setFixedHeight(2)
        self.grid.addWidget(line, row, 0, 1, 4)

    def _on_check(self, video_idx, res_idx, state):
        if state:
            # ألغ بقية مربعات نفس الصف
            for j, cb in enumerate(self.row_widgets.get(video_idx, [])):
                if j != res_idx and cb.isChecked():
                    cb.blockSignals(True); cb.setChecked(False); cb.blockSignals(False)
            self.selected_options[video_idx] = res_idx
        else:
            if video_idx in self.selected_options and self.selected_options[video_idx] == res_idx:
                del self.selected_options[video_idx]
        self._recalc_total()

    def _recalc_total(self):
        self.selected_options = {k: self.selected_options[k] for k in sorted(self.selected_options.keys())}
        use_ha = self.high_audio_cb.isChecked()
        use_hv = self.high_video_cb.isChecked()
        size_total = 0
        for k, v in self.selected_options.items():
            data = self.dict_all.get(k)
            if not data:
                continue
            sizes = data['heigh_size'] if use_hv else data['low_size']
            audio_idx = 1 if use_ha else 0
            if v < 2:
                size_total += sizes[v] if sizes[v] not in ("", None) else 0
            else:
                a = sizes[audio_idx] if sizes[audio_idx] not in ("", None) else 0
                vv = sizes[v] if sizes[v] not in ("", None) else 0
                size_total += a + vv
        self.size_btn.setText(f"{round(size_total, 2)} MB")
        self.download_btn.setEnabled(bool(self.selected_options))

    def _refresh_labels(self):
        # تحديث أحجام الفيديوهات على المربعات بحسب جودات الصوت/الفيديو
        use_ha = self.high_audio_cb.isChecked()
        use_hv = self.high_video_cb.isChecked()
        for i, data in self.dict_all.items():
            checks = self.row_widgets.get(i)
            if not checks:
                continue
            sizes = data['heigh_size'] if use_hv else data['low_size']
            for j in range(8):
                cb = checks[j]
                if j < len(sizes) and sizes[j] not in ("", None):
                    if j < 2:
                        txt = f"{_RES[j]} : {round(sizes[j], 2)} MB"
                    else:
                        audio_idx = 1 if use_ha else 0
                        a = sizes[audio_idx] if sizes[audio_idx] not in ("", None) else 0
                        txt = f"{_RES[j]} : {round(sizes[j] + a, 2)} MB"
                    cb.setText(txt)
                    cb.setEnabled(True)
                else:
                    cb.setText(f"{_RES[j]} : ❌")
                    cb.setEnabled(False)
        self._recalc_total()

    # ------------------------------- bulk select -------------------------- #
    def _bulk_select(self, select: bool):
        # تحديد فهرس الجودة المطلوبة بناءً على القائمة (Audio low=0, Audio high=1, ثم 144..1080 = 2..7)
        idx = self.bulk_quality.currentIndex()
        for i, checks in self.row_widgets.items():
            cb = checks[idx]
            if not cb.isEnabled():
                continue
            if select:
                if not cb.isChecked():
                    cb.setChecked(True)
            else:
                if cb.isChecked():
                    cb.setChecked(False)

    # ------------------------------- download all ------------------------- #
    def _press_download(self):
        if not self.selected_options:
            return
        try:
            with open(PATHS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            data = load_paths()
        path_list = data.get("path_list", default_downloads_dir())

        use_ha = self.high_audio_cb.isChecked()
        use_hv = self.high_video_cb.isChecked()
        folder = os.path.join(path_list, str(self.playlist_title or "Playlist"))
        try:
            os.makedirs(folder, exist_ok=True)
        except Exception:
            folder = path_list

        # إصلاح: استخدم مفاتيح القاموس الفعلية، لا i=range(len)
        for key, v in self.selected_options.items():
            data_item = self.dict_all.get(key)
            if not data_item:
                continue
            ids = data_item['heigh_id'] if use_hv else data_item['low_id']
            sizes = data_item['heigh_size'] if use_hv else data_item['low_size']
            info = data_item['info_process']
            url_item = data_item['url']
            audio_idx = 1 if use_ha else 0
            name = YouTubeDownloader().clean_filename(info[0] if info else "untitled")

            if v < 2:
                fmt = ids[v]
                ext = ".mp3"
                out = os.path.join(folder, f"{name}{ext}")
            else:
                if not ids[v] or not ids[audio_idx]:
                    continue
                fmt = f"{ids[audio_idx]}+{ids[v]}"
                if _is_facebook_url(url_item):
                    out = _facebook_video_output_path(folder, name, ".mp4")
                else:
                    out = os.path.join(folder, name)

            task = DownloadTask(
                url=url_item,
                format_id=fmt,
                output_path=out,
                flag=dict(self.flag),
                display_name=os.path.basename(out) or name,
                thumbnail_url=info[1] if info and len(info) > 1 else "",
            )
            DownloadManager.instance().add_task(task)

    # ------------------------------- reset/grid --------------------------- #
    def _reset_grid(self):
        # امسح الـ grid
        while self.grid.count():
            it = self.grid.takeAt(0)
            w = it.widget()
            if w is not None:
                w.setParent(None); w.deleteLater()
        self.row_widgets.clear()
        self.dict_all.clear()
        self.selected_options.clear()
        self.size_btn.setText("حجم المحدد")
        self.download_btn.setEnabled(False)

    def reset(self):
        """ريسيت كامل للشاشة: مسح كل البيانات وإرجاع الواجهة لحالتها الأولية."""
        # امسح الـ grid والبيانات
        self._reset_grid()
        # امسح روابط القائمة
        self.url = ""
        self.links = []
        self.playlist_title = ""
        # امسح خانات النطاق
        self.start_combo.clear()
        self.start_combo.addItem("بداية")
        self.end_combo.clear()
        self.end_combo.addItem("نهاية")
        # عطّل الأزرار
        self.analyze_btn.setEnabled(False)
        self.analyze_btn.setText("تحليل النطاق")
        self.pick_btn.setEnabled(True)
        self.pick_btn.setText("نسخ الرابط")
        # امسح خانات الاختيار
        try:
            self.high_audio_cb.setChecked(False)
            self.high_video_cb.setChecked(False)
            self.subtitle_cb.setChecked(False)
            self.cookies_cb.setChecked(False)
            self.subtitle_lang.setCurrentIndex(0)
        except Exception:
            pass
        # امسح الـ flag
        self.flag = {"op": False, "subtitle": False, "subtitle_lang": "ar"}



# ------------------ النافذة الرئيسية ------------------ #
TABS = [
    ("الرئيسية", "main"),
    ("التحميلات", "downloads"),
    ("تحميل الجميع", "force"),
    ("تحميل قائمة", "list"),
    ("الإعدادات", "settings"),
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(APP_TITLE)
        self.setFixedSize(1000, 700)

        central = QWidget()
        self.setCentralWidget(central)
        root = QVBoxLayout(central)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        top_bar = QFrame()
        top_bar.setObjectName("TopBar")
        top_bar.setFixedHeight(56)
        bar_layout = QHBoxLayout(top_bar)
        bar_layout.setContentsMargins(0, 0, 0, 0)
        bar_layout.setSpacing(0)
        root.addWidget(top_bar)

        self.stack = QStackedWidget()
        root.addWidget(self.stack, 1)

        self.pages = {
            "main": MainTab(),
            "downloads": DownloadsTab(),
            "force": ForceTab(),
            "list": ListTab(),
            "settings": SettingsTab(),
        }
        for key in ["main", "downloads", "force", "list", "settings"]:
            self.stack.addWidget(self.pages[key])

        self.tab_group = QButtonGroup(self)
        self.tab_group.setExclusive(True)
        self.tab_buttons = {}

        for i, (label, key) in enumerate(TABS):
            btn = QPushButton(label)
            btn.setObjectName("TabButton")
            btn.setCheckable(True)
            btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            btn.clicked.connect(lambda checked, k=key: self._switch_to(k))
            self.tab_group.addButton(btn, i)
            bar_layout.addWidget(btn, 1)
            self.tab_buttons[key] = btn

        self.tab_buttons["main"].setChecked(True)
        self.stack.setCurrentWidget(self.pages["main"])

        downloads_page = self.pages.get("downloads")
        if downloads_page is not None:
            if hasattr(downloads_page, "request_switch_to_self"):
                downloads_page.request_switch_to_self.connect(lambda: self._switch_to("downloads"))
            if hasattr(downloads_page, "request_switch_to_main"):
                downloads_page.request_switch_to_main.connect(self._open_main_and_analyze_memory)

        main_page = self.pages.get("main")
        if main_page is not None and hasattr(main_page, "request_force_analyze"):
            main_page.request_force_analyze.connect(self._open_force_and_analyze)

    def _switch_to(self, key):
        page = self.pages.get(key)
        if page is not None:
            self.stack.setCurrentWidget(page)
            btn = self.tab_buttons.get(key)
            if btn is not None:
                btn.setChecked(True)

    def _open_main_and_analyze_memory(self):
        """زر الرئيسية في التحميل المتعدد: ينتقل للرئيسية ثم يحلل رابط الحافظة إن كان صالحاً."""
        self._switch_to("main")
        try:
            url = pyperclip.paste().split("&")[0].strip()
        except Exception:
            url = ""
        if _is_valid_url(url):
            main_page = self.pages.get("main")
            if main_page is not None and hasattr(main_page, "start_analyze_for_url"):
                QTimer.singleShot(120, lambda u=url: main_page.start_analyze_for_url(u, show_warning=False))

    def _open_force_and_analyze(self, url: str):
        """تحويل روابط Facebook/SoundCloud إلى تحميل الجميع وبدء التحليل فوراً."""
        self._switch_to("force")
        force_page = self.pages.get("force")
        if force_page is not None and hasattr(force_page, "start_fetch_for_url"):
            QTimer.singleShot(80, lambda u=url: force_page.start_fetch_for_url(u))

    def closeEvent(self, event):
        # إغلاق آمن: إيقاف كل التحميلات والـ threads قدر الإمكان.
        try:
            DownloadManager.instance().shutdown()
        except Exception as e:
            print(f"shutdown error: {e}")

        # إيقاف مدير قائمة الانتظار (مراقبة الحافظة + ثريدات التحليل النشطة)
        # وثريدات الصور المصغّرة لبطاقاتها، إن كانت النافذة قد فُتحت من قبل.
        try:
            QueueManager.instance().shutdown()
            for page in self.pages.values():
                qdlg = getattr(page, "_queue_dialog", None)
                if qdlg is not None:
                    if hasattr(qdlg, "_save_size"):
                        qdlg._save_size()
                    qdlg.shutdown_threads()
        except Exception as e:
            print(f"queue shutdown error: {e}")

        try:
            for page in self.pages.values():
                active = getattr(page, "_active_threads", None)
                if active:
                    for (t, w) in list(active):
                        try:
                            # لو لدى العامل cancel نستدعيها.
                            if hasattr(w, "cancel"):
                                w.cancel()
                            t.quit()
                            t.wait(2500)
                        except Exception:
                            pass
                # Cookies thread الخاص بالإعدادات
                ck = getattr(page, "_ck_thread", None)
                if ck is not None:
                    try:
                        ck.quit(); ck.wait(2500)
                    except Exception:
                        pass
        except Exception as e:
            print(f"tabs shutdown error: {e}")
        try:
            if log and not log.closed:
                log.close()
        except Exception:
            pass
        super().closeEvent(event)


# ------------------ main ------------------ #
def main():
    myappid = 'AliDosouky.MGv4.PyQt6.4.3'
    if sys.platform.startswith("win"):
        try:
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        except Exception:
            pass

    app = QApplication(sys.argv)
    app.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
    app.setQuitOnLastWindowClosed(True)

    apply_theme(app)

    icon_path = find_app_icon_path("mg.ico")
    app_icon = QIcon(icon_path) if icon_path else QIcon()
    if not app_icon.isNull():
        # يجب ضبط أيقونة QApplication قبل إنشاء أي نافذة حتى يلتقطها نظام
        # التشغيل (شريط المهام) بشكل صحيح منذ اللحظة الأولى.
        app.setWindowIcon(app_icon)
    else:
        print("[icon] لم يتم العثور على ملف mg.ico في أي مسار معروف؛ "
              "ستظهر الأيقونة الافتراضية في شريط المهام وعنوان النافذة.")

    win = MainWindow()
    if not app_icon.isNull():
        win.setWindowIcon(app_icon)
    win.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()

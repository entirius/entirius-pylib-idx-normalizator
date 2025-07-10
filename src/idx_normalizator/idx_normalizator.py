import hashlib
import re

from slugify import slugify

IDX_ALLOWED_CHARS_PATTERN = re.compile(r"[^-a-z0-9_]+")


def normalize_idx(text: str, max_len: int = 128) -> str:
    assert text is not None, '"idx" can not be None'
    hash_len = 6  # dlugosc hasha
    separator = "_"
    idx = slugify(text, regex_pattern=IDX_ALLOWED_CHARS_PATTERN, separator="-")
    if len(idx) > max_len:
        prefix = idx[: max_len - hash_len - 1]
        rest = idx[max_len - hash_len - 1 :]
        rest = rest.encode("utf-8")
        m = hashlib.md5()
        m.update(rest)
        h = m.hexdigest()
        idx = "%s%s%s" % (prefix, separator, h[:hash_len])
    return idx


def validate_idx(idx: str, min_len=1, max_len=128):
    idx_normalized = normalize_idx(idx, max_len=max_len)
    if idx_normalized != idx:
        raise ValueError("idx must be slugify, maybe use normalize_idx()? {} != {}".format(idx_normalized, idx))
    if len(idx) < min_len:
        raise ValueError("idx must be {} min chars, idx={}".format(min_len, idx))
    if len(idx) > max_len:
        raise ValueError("idx must be {} max chars, idx={}".format(max_len, idx))


#
# PIM RealProduct SKU validator
# used also by Pricemanager etc
#
def normalize_sku(sku) -> str:
    assert sku is not None, '"sku" can not be None'
    return str(sku).strip()


def validate_sku(sku):
    """
    https://docs.lazelab.cloud/functional-areas/products-catalog/sku-format.html
    """
    min_len = 1
    max_len = 128
    forbidden_chars = [","]
    sku_normalized = normalize_sku(sku)
    if sku_normalized != sku:
        raise ValueError("sku must be striped, maybe use normalize_sku()? {} != {}".format(sku_normalized, sku))
    for char in forbidden_chars:
        index = sku.find(char)
        if index != -1:
            raise ValueError('SKU contains forbidden character="{}" sku={}'.format(char, sku))
    if len(sku) < min_len:
        raise ValueError("SKU must be {} min chars, sku={}".format(min_len, sku))
    if len(sku) > max_len:
        raise ValueError("SKU must be {} max chars, sku={}".format(max_len, sku))


def normalize_ean(ean):
    if not ean:  # None or ""
        return None
    return str(ean).lower().strip()


def validate_ean(ean, min_len=8, max_len=16):
    if not ean:
        return
    ean_normalized = normalize_ean(ean)
    if ean_normalized != ean:
        raise ValueError("ean must be lower and strip, maybe use normalize_ean()? {} != {}".format(ean_normalized, ean))
    if len(ean) < min_len:
        raise ValueError("ean must be {} min chars, ean={}".format(min_len, ean))
    if len(ean) > max_len:
        raise ValueError("ean must be {} max chars, ean={}".format(max_len, ean))


def normalize_url_key(url_key):
    """In Magento "url_key" is striped, lower, and "-" is used as separator"""
    separator = "-"
    if url_key is None:
        raise Exception('ProductCategory "url_key" can not be None')
    url_key = url_key.strip()
    url_key = url_key.lower()
    url_key = slugify(url_key, separator=separator)
    return url_key


def validate_url_key(url_key):
    orig = url_key
    url_key = normalize_url_key(url_key)
    if url_key != orig:
        raise Exception(
            'ProductCategory "url_key" must be striped and lowered and slugified, maybe use normalize_url_key()? {} != {}'.format(
                url_key, orig
            )
        )

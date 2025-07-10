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
        idx = f"{prefix}{separator}{h[:hash_len]}"
    return idx


def validate_idx(idx: str, min_len=1, max_len=128):
    idx_normalized = normalize_idx(idx, max_len=max_len)
    if idx_normalized != idx:
        raise ValueError(
            f"idx must be slugify, maybe use normalize_idx()? {idx_normalized} != {idx}"
        )
    if len(idx) < min_len:
        raise ValueError(f"idx must be {min_len} min chars, idx={idx}")
    if len(idx) > max_len:
        raise ValueError(f"idx must be {max_len} max chars, idx={idx}")


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
        raise ValueError(
            f"sku must be striped, maybe use normalize_sku()? {sku_normalized} != {sku}"
        )
    for char in forbidden_chars:
        index = sku.find(char)
        if index != -1:
            raise ValueError(f'SKU contains forbidden character="{char}" sku={sku}')
    if len(sku) < min_len:
        raise ValueError(f"SKU must be {min_len} min chars, sku={sku}")
    if len(sku) > max_len:
        raise ValueError(f"SKU must be {max_len} max chars, sku={sku}")


def normalize_ean(ean):
    if not ean:  # None or ""
        return None
    return str(ean).lower().strip()


def validate_ean(ean, min_len=8, max_len=16):
    if not ean:
        return
    ean_normalized = normalize_ean(ean)
    if ean_normalized != ean:
        raise ValueError(
            f"ean must be lower and strip, maybe use normalize_ean()? "
            f"{ean_normalized} != {ean}"
        )
    if len(ean) < min_len:
        raise ValueError(f"ean must be {min_len} min chars, ean={ean}")
    if len(ean) > max_len:
        raise ValueError(f"ean must be {max_len} max chars, ean={ean}")


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
            f'ProductCategory "url_key" must be striped and lowered and '
            f"slugified, maybe use normalize_url_key()? {url_key} != {orig}"
        )

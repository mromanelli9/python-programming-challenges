#!/usr/bin/env python

def not_implemented(f, *args, **kwargs):
    try:
        f(*args, **kwargs)
        return False
    except Exception as e:
        if isinstance(e, NotImplementedError):
            return True
        else:
            return False

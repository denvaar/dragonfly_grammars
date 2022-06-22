from dragonfly import Choice

def elixir_enum_choice(name):
    return Choice(name, {
        "all": "all?",
        "any": "any?",
        "at": "at",
        "chunk by": "chunk_by",
        "chunk every": "chunk_every",
        "chunk while": "chunk_while",
        "kun cat": "concat",
        "count": "count",
        "count until": "count_until",
        "D dupe": "dedup",
        "D dupe by": "dedup_by",
        "drop": "drop",
        "drop every": "drop_every",
        "drop while": "drop_while",
        "each": "each",
        "empty": "empty?",
        "fetch": "fetch",
        "fetch": "fetch!",
        "filter": "filter",
        "find": "find",
        "find index": "find_index",
        "find value": "find_value",
        "flat map": "flat_map",
        "flat map reduce": "flat_map_reduce",
        "frequencies": "frequencies",
        "frequencies by": "frequencies_by",
        "group by": "group_by",
        "intersperse": "intersperse",
        "in to": "into",
        "join": "join",
        "map": "map",
        "map every": "map_every",
        "map intersperse": "map_intersperse",
        "map join": "map_join",
        "map reduce": "map_reduce",
        "max": "max",
        "max by": "max_by",
        "member": "member?",
        "min": "min",
        "min by": "min_by",
        "min max": "min_max",
        "min max by": "min_max_by",
        "product": "product",
        "random": "random",
        "reduce": "reduce",
        "reduce while": "reduce_while",
        "reject": "reject",
        "reverse": "reverse",
        "reverse slice": "reverse_slice",
        "scan": "scan",
        "shuffle": "shuffle",
        "slice": "slice",
        "slide": "slide",
        "sort": "sort",
        "sort by": "sort_by",
        "split": "split",
        "split while": "split_while",
        "split with": "split_with",
        "sum": "sum",
        "take": "take",
        "take every": "take_every",
        "take random": "take_random",
        "take while": "take_while",
        "to list": "to_list",
        "unique": "uniq",
        "unique by": "uniq_by",
        "unzip": "unzip",
        "with index": "with_index",
        "zip": "zip",
        "zip reduce": "zip_reduce",
        "zip with": "zip_with",
    }, default="")


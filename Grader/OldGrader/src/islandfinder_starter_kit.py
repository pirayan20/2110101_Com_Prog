import numpy as np


def to_cluster(a: np.array):
    """
    Seperate cluster from 2d array.

    # Parameters
    a: array_like - 2 dimension array of `True` or `False` with dtype np.bool.

    # Returns
    cluster_list: List - a list of 2d array each with only one cluster.

    # Notes
    This function doesn't guarantee order of output.

    # Examples
    >>> a = np.array([
                [1, 0, 1],
                [1, 0, 1],
                [1, 0, 1],
            ], np.bool)
    >>> np.array(to_cluster(a))
    array([[[ True, False, False],
            [ True, False, False],
            [ True, False, False]],
           [[False, False,  True],
            [False, False,  True],
            [False, False,  True]]])
    """
    height, width = a.shape
    output = []
    last_cross_section = []
    start_row = np.argmax(np.pad(np.max(a, axis=1), ((0, 1),), mode='constant', constant_values=np.inf))
    for row_index in range(start_row, height):
        cross_section = []
        seg_start = np.argmax(np.pad(a[row_index], ((0, 1),), mode='constant', constant_values=np.inf))
        for col_index in range(seg_start, width + 1):
            if (col_index == width and a[row_index][col_index-1]) or (col_index < width and a[row_index][col_index-1] and not a[row_index][col_index]):
                seg = np.full_like(a, False)
                seg[row_index, seg_start:col_index] = True
                cross_section.append(seg)
            if col_index < width and not a[row_index][col_index-1] and a[row_index][col_index]:
                seg_start = col_index
        marked_remove = set()
        for lcs in last_cross_section:
            merged_to = None
            for ic, ccs in enumerate(cross_section):
                if np.any(np.logical_and(lcs[row_index - 1], ccs[row_index])):
                    if merged_to is None:
                        ccs[:, :] = np.logical_or(lcs, ccs)  # inplace merge
                        merged_to = ccs
                    else:  # merge into the same lcs, so need to remove from last_cross_section
                        merged_to[:, :] = np.logical_or(merged_to, ccs)  # inplace merge
                        marked_remove.add(ic)
            if merged_to is None:
                output.append(lcs)
        last_cross_section = [cross_section[ic] for ic in range(len(cross_section)) if ic not in marked_remove]
    output.extend(last_cross_section)
    return output

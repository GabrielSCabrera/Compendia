import numpy as np

def tex_table(a, caption, label, titles, vbars = None, hbars = None,
sigfigs = 0.3):
    '''
        Automatically formats a LaTEX compatible table with a high degree of
        customizability.

        <a> should be a numpy array of dimension (m,n) for m columns each of
        length n.

        <caption> should be a string, which will be the figure text
        displayed in LaTEX.

        <label> is the LaTEX reference label, which can be
        used to refer to this figure in another part of the file.

        <titles> should be a list of length m, containing the titles for each
        column of the table.

        <vbars> (which is an optional parameter) must be an array of length m+1
        of ones and zeros where a one represents a vertical bar in the chart,
        and zero represents a lack thereof.  By default, it will be of the form
        [1, 0, 0, ..., 0, 1].

        <hbars> (which is an optional parameter) must be an array of length n
        of ones and zeros where a one represents a vertical bar in the chart,
        and zero represents a lack thereof.  By default, it will be of the form
        [1, 0, 0, ..., 0, 1].

        <sigfigs> (which is an optional parameter) may be an integer OR an array
        of length m, with a particular significant figure for each column of
        data.  Note - these values should be in terms that can be interpreted
        in string formatting syntax (for example 0.1 for 1 sigfig after the dot).
    '''
    a_len = len(a)
    titles_len = len(titles)
    if a_len > titles_len:
        titles += ['']*(a_len - titles_len)
    if hbars is None:
        hbars = np.zeros(len(a[0]))
        hbars[-1] = 1
    if isinstance(sigfigs, (float, int)):
        sigfigs = np.ones(a_len)*sigfigs
    string = r'\begin{figure}[H]'
    string += '\n\\centering\n'
    string += '\\caption{{{}\\label{{{}}}}}\n'.format(caption, label)
    string += r'\begin{tabular}{'
    if vbars is None:
        string += '|c'*a_len
        string += '|}'
    else:
        for n,i in enumerate(vbars):
            if n == 0:
                if i == 1:
                    string += '|'
            elif i == 0:
                string += 'c'
            elif i == 1:
                string += 'c|'
        string += '}'
    string += '\n\\hline\n'
    for n, title in enumerate(titles):
        string += '{} '.format(title)
        if n < a_len - 1:
            string += '& '
    string += '\\\\\n\\hline\n\\hline\n'
    for i in range(len(a[0])):
        for n,(j,k) in enumerate(zip(a[:,i], sigfigs)):
            if isinstance(j, (int, float)):
                string += '{:{width}f} '.format(j, width = k)
            else:
                string += '{} '.format(j)
            if n < a_len - 1:
                string += '& '
        if hbars[i] == 1:
            string += '\\\\\n\\hline\n'
        elif hbars[i] == 0:
            string += '\\\\\n\n'
    string += r'\end{tabular}'
    string += '\n'
    string += r'\end{figure}'
    return string

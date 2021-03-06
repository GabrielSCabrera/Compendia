import numpy as np
cu_imp = False
try:
    import Class_uncertainty as cU
    cu_imp = True
except:
    pass

def tex_table(a, caption, label, titles, vbars = None, hbars = None,
sigfigs = None):
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
        of zeros, ones and twos where a one represents a horizontal bar in the
        chart and zero represents a lack thereof; two represents a double-bar.
        By default, it will be of the form [1, 0, 0, ..., 0, 1].

        <sigfigs> (which is an optional parameter) may be an integer OR an array
        of length m, with a particular significant figure for each column of
        data.  Note - these values should be in terms that can be interpreted
        in string formatting syntax (for example 0.1 for 1 sigfig after the dot).
    '''
    if sigfigs is None:
        sigfigs = 0.2
        nosigfigs = True
    else:
        nosigfigs = False
    a_len = len(a)
    titles_len = len(titles)
    if a_len > titles_len:
        titles += ['']*(a_len - titles_len)
    if hbars is None:
        hbars = np.zeros(len(a[0]))
        hbars[-1] = 1
    if isinstance(sigfigs, (float, int)):
        sigfigs = np.ones(a_len)*sigfigs
    string = r'\begin{table}[H]'
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

                string += '{:{width}f} '.format(float(j), width = k)
            elif cu_imp is True and isinstance(j, (cU.uFloat)):
                if nosigfigs is True:
                    temp = '{}'.format(j)
                else:
                    temp = '{:{width}g} '.format(j, width = k)
                temp = (temp.split('±'))
                temp[0], temp[1] = temp[0].strip(), temp[1].strip()
                if j.uncertainty != 0:
                    for m,l in enumerate(temp[0]):
                        if l == 'e':
                            if float(temp[0][:m]) == 1:
                                temp[0] = r'10^{' + str(int(temp[0][m+1:])) + '}'
                            else:
                                temp[0] = temp[0][:m] + r' \times 10^{' + str(int(temp[0][m+1:])) + '}'
                            break
                    for m,l in enumerate(temp[1]):
                        if l == 'e':
                            if float(temp[1][:m]) == 1:
                                temp[1] = r'10^{' + str(int(temp[1][m+1:])) + '}'
                            else:
                                temp[1] = temp[1][:m] + r' \times 10^{' + str(int(temp[1][m+1:])) + '}'
                            break
                    string += '$' + temp[0] + ' \pm ' + temp[1] + '$ '
                else:
                    string += '$' + temp[0] + '$ '
            else:
                string += '{} '.format(j)
            if n < a_len - 1:
                string += '& '
        if hbars[i] == 2:
            string += '\\\\\n\\hline\n\\hline\n'
        elif hbars[i] == 1:
            string += '\\\\\n\\hline\n'
        elif hbars[i] == 0:
            string += '\\\\\n'
    string += r'\end{tabular}'
    string += '\n'
    string += r'\end{table}'
    return string

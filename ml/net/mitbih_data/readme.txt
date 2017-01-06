This data comes from the MITBIH Arrhythmia database. 

Downloaded from:
http://www.physionet.org/physiobank/database/mitdb/

dowload_data.py will download all the MITBIH arrhythmia files. Use python2 for this.

File types downloaded:
 - .dat -- signals
 - .atr -- annotations
 - .hea -- header files

Samples recorded at 11-bit resolution over a 10mV range
 - i.e. 2^11=2048 steps, each separated by 10/2048=0.0049mV

Downloaded files can be read using WFDB (pip install wfdb)
 - I found the function documentation (and annotation definitions) in their repository code:
   https://github.com/MIT-LCP/wfdb-python


Copying the annotation definitions here:

  INDEX: 'SYMBOL'     #DESCRIPTION
    0: ' ',  # not-QRS (not a getann/putann codedict) */
    1: 'N',  # normal beat */
    2: 'L',  # left bundle branch block beat */
    3: 'R',  # right bundle branch block beat */
    4: 'a',  # aberrated atrial premature beat */
    5: 'V',  # premature ventricular contraction */
    6: 'F',  # fusion of ventricular and normal beat */
    7: 'J',  # nodal (junctional) premature beat */
    8: 'A',  # atrial premature contraction */
    9: 'S',  # premature or ectopic supraventricular beat */
    10: 'E',  # ventricular escape beat */
    11: 'j',  # nodal (junctional) escape beat */
    12: '/',  # paced beat */
    13: 'Q',  # unclassifiable beat */
    14: '~',  # signal quality change */
    15: '[15]',
    16: '|',  # isolated QRS-like artifact */
    17: '[17]',
    18: 's',  # ST change */
    19: 'T',  # T-wave change */
    20: '*',  # systole */
    21: 'D',  # diastole */
    22: '"',  # comment annotation */
    23: '=',  # measurement annotation */
    24: 'p',  # P-wave peak */
    25: 'B',  # left or right bundle branch block */
    26: '^',  # non-conducted pacer spike */
    27: 't',  # T-wave peak */
    28: '+',  # rhythm change */
    29: 'u',  # U-wave peak */
    30: '?',  # learning */
    31: '!',  # ventricular flutter wave */
    32: '[',  # start of ventricular flutter/fibrillation */
    33: ']',  # end of ventricular flutter/fibrillation */
    34: 'e',  # atrial escape beat */
    35: 'n',  # supraventricular escape beat */
    36: '@',  # link to external data (aux contains URL) */
    37: 'x',  # non-conducted P-wave (blocked APB) */
    38: 'f',  # fusion of paced and normal beat */
    39: '(',  # waveform onset */
    # 39: 'PQ', # PQ junction (beginning of QRS) */
    40: ')',  # waveform end */
    # 40: 'JPT', # J point (end of QRS) */
    41: 'r',  # R-on-T premature ventricular contraction */
    42: '[42]',
    43: '[43]',
    44: '[44]',
    45: '[45]',
    46: '[46]',
    47: '[47]',
    48: '[48]',
    49: '[49]'

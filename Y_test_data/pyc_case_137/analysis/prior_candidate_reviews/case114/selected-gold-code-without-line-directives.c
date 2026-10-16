psutil_proc_cpu_affinity_get(PyObject *self, PyObject *args)
{
    int cpu, ncpus, count, cpucount_s;
    long pid;
    size_t setsize;
    cpu_set_t *mask = 
                     ((void *)0)
                         ;
    PyObject *res = 
                   ((void *)0)
                       ;

    if (!PyArg_ParseTuple(args, "i", &pid))
        return 
              ((void *)0)
                  ;
    ncpus = NCPUS_START;
    while (1) {
        setsize = 
                 ((((
                 ncpus
                 ) + (8 * sizeof (__cpu_mask)) - 1) / (8 * sizeof (__cpu_mask))) * sizeof (__cpu_mask))
                                      ;
        mask = 
              __sched_cpualloc (
              ncpus
              )
                              ;
        if (mask == 
                   ((void *)0)
                       )
            return PyErr_NoMemory();
        if (sched_getaffinity(pid, setsize, mask) == 0)
            break;
        
       __sched_cpufree (
       mask
       )
                     ;
        if (
           (*__errno_location ()) 
                 != 
                    22
                          )
            return PyErr_SetFromErrno(PyExc_OSError);
        if (ncpus > 0x7fffffff / 2) {
            PyErr_SetString(PyExc_OverflowError, "could not allocate "
                            "a large enough CPU set");
            return 
                  ((void *)0)
                      ;
        }
        ncpus = ncpus * 2;
    }

    res = PyList_New(0);
    if (res == 
              ((void *)0)
                  )
        goto error;

    cpucount_s = 
                __sched_cpucount (
                setsize
                , 
                mask
                )
                                          ;
    for (cpu = 0, count = cpucount_s; count; cpu++) {
        if (
           (__extension__ ({ size_t __cpu = (
           cpu
           ); __cpu / 8 < (
           setsize
           ) ? ((((const __cpu_mask *) ((
           mask
           )->__bits))[((__cpu) / (8 * sizeof (__cpu_mask)))] & ((__cpu_mask) 1 << ((__cpu) % (8 * sizeof (__cpu_mask)))))) != 0 : 0; }))
                                          ) {

            PyObject *cpu_num = PyLong_FromLong(cpu);



            if (cpu_num == 
                          ((void *)0)
                              )
                goto error;
            if (PyList_Append(res, cpu_num)) {
                _Py_DECREF("/source/_psutil_linux.c", 310, ((PyObject*)(cpu_num)));
                goto error;
            }
            _Py_DECREF("/source/_psutil_linux.c", 313, ((PyObject*)(cpu_num)));
            --count;
        }
    }
    
   __sched_cpufree (
   mask
   )
                 ;
    return res;

error:
    if (mask)
        
       __sched_cpufree (
       mask
       )
                     ;
    _Py_XDECREF(((PyObject*)(res)));
    return 
          ((void *)0)
              ;
}

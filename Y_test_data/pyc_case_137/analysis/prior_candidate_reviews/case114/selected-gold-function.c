psutil_proc_cpu_affinity_get(PyObject *self, PyObject *args)
{
    int cpu, ncpus, count, cpucount_s;
    long pid;
    size_t setsize;
    cpu_set_t *mask = 
# 271 "/source/_psutil_linux.c" 3 4
                     ((void *)0)
# 271 "/source/_psutil_linux.c"
                         ;
    PyObject *res = 
# 272 "/source/_psutil_linux.c" 3 4
                   ((void *)0)
# 272 "/source/_psutil_linux.c"
                       ;

    if (!PyArg_ParseTuple(args, "i", &pid))
        return 
# 275 "/source/_psutil_linux.c" 3 4
              ((void *)0)
# 275 "/source/_psutil_linux.c"
                  ;
    ncpus = NCPUS_START;
    while (1) {
        setsize = 
# 278 "/source/_psutil_linux.c" 3 4
                 ((((
# 278 "/source/_psutil_linux.c"
                 ncpus
# 278 "/source/_psutil_linux.c" 3 4
                 ) + (8 * sizeof (__cpu_mask)) - 1) / (8 * sizeof (__cpu_mask))) * sizeof (__cpu_mask))
# 278 "/source/_psutil_linux.c"
                                      ;
        mask = 
# 279 "/source/_psutil_linux.c" 3 4
              __sched_cpualloc (
# 279 "/source/_psutil_linux.c"
              ncpus
# 279 "/source/_psutil_linux.c" 3 4
              )
# 279 "/source/_psutil_linux.c"
                              ;
        if (mask == 
# 280 "/source/_psutil_linux.c" 3 4
                   ((void *)0)
# 280 "/source/_psutil_linux.c"
                       )
            return PyErr_NoMemory();
        if (sched_getaffinity(pid, setsize, mask) == 0)
            break;
        
# 284 "/source/_psutil_linux.c" 3 4
       __sched_cpufree (
# 284 "/source/_psutil_linux.c"
       mask
# 284 "/source/_psutil_linux.c" 3 4
       )
# 284 "/source/_psutil_linux.c"
                     ;
        if (
# 285 "/source/_psutil_linux.c" 3 4
           (*__errno_location ()) 
# 285 "/source/_psutil_linux.c"
                 != 
# 285 "/source/_psutil_linux.c" 3 4
                    22
# 285 "/source/_psutil_linux.c"
                          )
            return PyErr_SetFromErrno(PyExc_OSError);
        if (ncpus > 0x7fffffff / 2) {
            PyErr_SetString(PyExc_OverflowError, "could not allocate "
                            "a large enough CPU set");
            return 
# 290 "/source/_psutil_linux.c" 3 4
                  ((void *)0)
# 290 "/source/_psutil_linux.c"
                      ;
        }
        ncpus = ncpus * 2;
    }

    res = PyList_New(0);
    if (res == 
# 296 "/source/_psutil_linux.c" 3 4
              ((void *)0)
# 296 "/source/_psutil_linux.c"
                  )
        goto error;

    cpucount_s = 
# 299 "/source/_psutil_linux.c" 3 4
                __sched_cpucount (
# 299 "/source/_psutil_linux.c"
                setsize
# 299 "/source/_psutil_linux.c" 3 4
                , 
# 299 "/source/_psutil_linux.c"
                mask
# 299 "/source/_psutil_linux.c" 3 4
                )
# 299 "/source/_psutil_linux.c"
                                          ;
    for (cpu = 0, count = cpucount_s; count; cpu++) {
        if (
# 301 "/source/_psutil_linux.c" 3 4
           (__extension__ ({ size_t __cpu = (
# 301 "/source/_psutil_linux.c"
           cpu
# 301 "/source/_psutil_linux.c" 3 4
           ); __cpu / 8 < (
# 301 "/source/_psutil_linux.c"
           setsize
# 301 "/source/_psutil_linux.c" 3 4
           ) ? ((((const __cpu_mask *) ((
# 301 "/source/_psutil_linux.c"
           mask
# 301 "/source/_psutil_linux.c" 3 4
           )->__bits))[((__cpu) / (8 * sizeof (__cpu_mask)))] & ((__cpu_mask) 1 << ((__cpu) % (8 * sizeof (__cpu_mask)))))) != 0 : 0; }))
# 301 "/source/_psutil_linux.c"
                                          ) {

            PyObject *cpu_num = PyLong_FromLong(cpu);



            if (cpu_num == 
# 307 "/source/_psutil_linux.c" 3 4
                          ((void *)0)
# 307 "/source/_psutil_linux.c"
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
    
# 317 "/source/_psutil_linux.c" 3 4
   __sched_cpufree (
# 317 "/source/_psutil_linux.c"
   mask
# 317 "/source/_psutil_linux.c" 3 4
   )
# 317 "/source/_psutil_linux.c"
                 ;
    return res;

error:
    if (mask)
        
# 322 "/source/_psutil_linux.c" 3 4
       __sched_cpufree (
# 322 "/source/_psutil_linux.c"
       mask
# 322 "/source/_psutil_linux.c" 3 4
       )
# 322 "/source/_psutil_linux.c"
                     ;
    _Py_XDECREF(((PyObject*)(res)));
    return 
# 324 "/source/_psutil_linux.c" 3 4
          ((void *)0)
# 324 "/source/_psutil_linux.c"
              ;
}

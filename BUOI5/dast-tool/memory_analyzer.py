import gc
import tracemalloc


class MemoryAnalyzer:
    def __init__(self):
        if not tracemalloc.is_tracing():
            tracemalloc.start()
        gc.collect()
        self.baseline = tracemalloc.get_traced_memory()[0]

    def check_memory_leaks(self):
        gc.collect()
        current, peak = tracemalloc.get_traced_memory()
        return dict(current_bytes=current, peak_bytes=peak, growth_bytes=current-self.baseline,
                    uncollectable_objects=len(gc.garbage),
                    note='Growth is an observation, not proof of a memory leak.')

    def check_overflow(self, value):
        return isinstance(value, int) and not isinstance(value, bool) and not -(2**63) <= value <= 2**63-1

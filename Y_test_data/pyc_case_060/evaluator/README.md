# Evaluator

Candidate patch is applied before the exact protected official test patch, then native extensions are forcibly rebuilt. Four unchanged official nodes run separately using the isolated helper; each child executes pytest_no_dump.py before pytest.main. Native process signals are retained and graded as failures. The final runtime configuration explicitly mounts both helpers.

The exact upstream linear/radial tests loop L, P, I and F, compare generated pixels against existing PNG references and check key pixels/modes. Base terminates at I, so F is not reached on Base; Gold verifies both I and F. Two unchanged RGB wrong-mode nodes preserve ValueError behavior. Official test logic is unmodified. Each node runs in a separate subprocess; native SIGSEGV is recorded as process failure rather than an assertion, aggregate exit 1 permits complete node grading. The product patch changes C Fill.c only; no binary asset changes.

NumPy is not required; its inherited template config argument is unused.

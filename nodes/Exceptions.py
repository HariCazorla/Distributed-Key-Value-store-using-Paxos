class InvalidPathException(Exception):
    """
    Exception when invalid URL path
    """
    pass


class PrepareRequestMajorityException(Exception):
    """
    Exception thrown when majority of peers do not
    acknowledge for the prepare request
    """


class InvalidProposalNumberException(Exception):
    """
    Exception thrown when prepare request does not 
    have a proper proposal uuid number
    """


class AcceptRequestMajorityException(Exception):
    """
    Exception thrown when majority of peers do not
    acknowledge for the Accept request
    """


class UnexpectedException(Exception):
    """
    Exception due to unexpected reasons
    """
    pass

# These paramaters should be received from Perspective form elements
vatPercentage = 15  # form element should be editable, but should default to 15
vatExclusive = 100
vatInclusive = 115

# Requires the user to have entered an amount that includes VAT
def getVatExclusive():
    result = vatInclusive / (1 + vatPercentage/100)
    return str(round(result,2))

# Requires the user to have entered an amount that excludes VAT
def getVatInclusive():
    result = vatExclusive + vatExclusive * (vatPercentage/100)
    return str(round(result,2))
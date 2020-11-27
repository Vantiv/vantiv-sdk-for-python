from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

__NAMESPACE__ = "http://www.vantivcnp.com/schema"


@dataclass
class RFRResponse:
    """
    :ivar response:
    :ivar message:
    """
    class Meta:
        namespace = "http://www.vantivcnp.com/schema"

    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class AccountInfoType:
    """
    :ivar type:
    :ivar number:
    """
    class Meta:
        name = "accountInfoType"

    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class AccountUpdateFileRequestData:
    """
    :ivar merchantId:
    :ivar postDay:
    """
    class Meta:
        name = "accountUpdateFileRequestData"
        namespace = "http://www.vantivcnp.com/schema"

    merchantId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDay: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class AdvancedFraudChecksType:
    """
    :ivar threatMetrixSessionId:
    :ivar webSessionId:
    :ivar customAttribute1:
    :ivar customAttribute2:
    :ivar customAttribute3:
    :ivar customAttribute4:
    :ivar customAttribute5:
    """
    class Meta:
        name = "advancedFraudChecksType"

    threatMetrixSessionId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    webSessionId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    customAttribute1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    customAttribute2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    customAttribute3: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    customAttribute4: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    customAttribute5: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class AdvancedFraudResultsType:
    """
    :ivar deviceReviewStatus:
    :ivar deviceReputationScore:
    :ivar triggeredRule:
    """
    class Meta:
        name = "advancedFraudResultsType"

    deviceReviewStatus: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    deviceReputationScore: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    triggeredRule: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class AndroidpayResponse:
    """
    :ivar cryptogram:
    :ivar expMonth:
    :ivar expYear:
    :ivar eciIndicator:
    """
    class Meta:
        name = "androidpayResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cryptogram: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    expMonth: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    expYear: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    eciIndicator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class ApplepayHeaderType:
    """
    :ivar applicationData:
    :ivar ephemeralPublicKey:
    :ivar publicKeyHash:
    :ivar transactionId:
    """
    class Meta:
        name = "applepayHeaderType"

    applicationData: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    ephemeralPublicKey: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    publicKeyHash: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    transactionId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class ApplepayResponse:
    """
    :ivar applicationPrimaryAccountNumber:
    :ivar applicationExpirationDate:
    :ivar currencyCode:
    :ivar transactionAmount:
    :ivar cardholderName:
    :ivar deviceManufacturerIdentifier:
    :ivar paymentDataType:
    :ivar onlinePaymentCryptogram:
    :ivar eciIndicator:
    """
    class Meta:
        name = "applepayResponse"
        namespace = "http://www.vantivcnp.com/schema"

    applicationPrimaryAccountNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    applicationExpirationDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    currencyCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    transactionAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    cardholderName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    deviceManufacturerIdentifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    paymentDataType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    onlinePaymentCryptogram: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    eciIndicator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Authentication:
    """
    :ivar user:
    :ivar password:
    """
    class Meta:
        name = "authentication"
        namespace = "http://www.vantivcnp.com/schema"

    user: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    password: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class CardAccountInfoType:
    """
    :ivar type:
    :ivar number:
    :ivar expDate:
    """
    class Meta:
        name = "cardAccountInfoType"

    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    expDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class CardOrToken:
    """
    :ivar anyElement:
    """
    class Meta:
        name = "cardOrToken"
        namespace = "http://www.vantivcnp.com/schema"

    anyElement: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class CardPaypageType:
    """
    :ivar paypageRegistrationId:
    :ivar expDate:
    :ivar cardValidationNum:
    :ivar type:
    """
    class Meta:
        name = "cardPaypageType"

    paypageRegistrationId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    expDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    cardValidationNum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class CardTokenInfoType:
    """
    :ivar cnpToken:
    :ivar type:
    :ivar expDate:
    :ivar bin:
    """
    class Meta:
        name = "cardTokenInfoType"

    cnpToken: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    expDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    bin: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class CardTokenType:
    """
    :ivar cnpToken:
    :ivar tokenUrl:
    :ivar expDate:
    :ivar cardValidationNum:
    :ivar type:
    :ivar checkoutId:
    :ivar authenticatedShopperId:
    """
    class Meta:
        name = "cardTokenType"

    cnpToken: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    tokenUrl: Optional[str] = field(
        default=None,
        metadata={
            "name": "tokenURL",
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    expDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    cardValidationNum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    checkoutId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    authenticatedShopperId: Optional[str] = field(
        default=None,
        metadata={
            "name": "authenticatedShopperID",
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class CardType:
    """
    :ivar type:
    :ivar number:
    :ivar expDate:
    :ivar track:
    :ivar cardValidationNum:
    :ivar pin:
    """
    class Meta:
        name = "cardType"

    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    expDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    track: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    cardValidationNum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    pin: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class CnpInternalRecurringRequestType:
    """
    :ivar subscriptionId:
    :ivar recurringTxnId:
    :ivar finalPayment:
    """
    class Meta:
        name = "cnpInternalRecurringRequestType"

    subscriptionId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    recurringTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    finalPayment: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class CnpTransactionInterface:
    class Meta:
        name = "cnpTransactionInterface"


@dataclass
class Contact:
    """
    :ivar name:
    :ivar firstName:
    :ivar middleInitial:
    :ivar lastName:
    :ivar companyName:
    :ivar addressLine1:
    :ivar addressLine2:
    :ivar addressLine3:
    :ivar city:
    :ivar state:
    :ivar zip:
    :ivar country:
    :ivar email:
    :ivar phone:
    """
    class Meta:
        name = "contact"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    firstName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    middleInitial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    lastName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    companyName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    addressLine1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    addressLine2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    addressLine3: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    state: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    zip: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    phone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class CreateAddOnType:
    """
    :ivar addOnCode:
    :ivar name:
    :ivar amount:
    :ivar startDate:
    :ivar endDate:
    """
    class Meta:
        name = "createAddOnType"

    addOnCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    startDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    endDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class CreateDiscountType:
    """
    :ivar discountCode:
    :ivar name:
    :ivar amount:
    :ivar startDate:
    :ivar endDate:
    """
    class Meta:
        name = "createDiscountType"

    discountCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    startDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    endDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class CtxPaymentInformationType:
    """
    :ivar ctxPaymentDetail:
    """
    class Meta:
        name = "ctxPaymentInformationType"

    ctxPaymentDetail: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class CustomBilling:
    """
    :ivar phone:
    :ivar city:
    :ivar url:
    :ivar descriptor:
    """
    class Meta:
        name = "customBilling"
        namespace = "http://www.vantivcnp.com/schema"

    phone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    descriptor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class CustomerInfo:
    """
    :ivar ssn:
    :ivar dob:
    :ivar customerRegistrationDate:
    :ivar customerType:
    :ivar incomeAmount:
    :ivar incomeCurrency:
    :ivar customerCheckingAccount:
    :ivar customerSavingAccount:
    :ivar employerName:
    :ivar customerWorkTelephone:
    :ivar residenceStatus:
    :ivar yearsAtResidence:
    :ivar yearsAtEmployer:
    """
    class Meta:
        name = "customerInfo"
        namespace = "http://www.vantivcnp.com/schema"

    ssn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    dob: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    customerRegistrationDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    customerType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    incomeAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    incomeCurrency: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    customerCheckingAccount: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    customerSavingAccount: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    employerName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    customerWorkTelephone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    residenceStatus: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    yearsAtResidence: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    yearsAtEmployer: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class DeleteAddOnType:
    """
    :ivar addOnCode:
    """
    class Meta:
        name = "deleteAddOnType"

    addOnCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class DeleteDiscountType:
    """
    :ivar discountCode:
    """
    class Meta:
        name = "deleteDiscountType"

    discountCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class DetailTax:
    """
    :ivar taxIncludedInTotal:
    :ivar taxAmount:
    :ivar taxRate:
    :ivar taxTypeIdentifier:
    :ivar cardAcceptorTaxId:
    """
    class Meta:
        name = "detailTax"
        namespace = "http://www.vantivcnp.com/schema"

    taxIncludedInTotal: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    taxAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    taxRate: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    taxTypeIdentifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    cardAcceptorTaxId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class DriversLicenseInfo:
    """
    :ivar licenseNumber:
    :ivar state:
    :ivar dateOfBirth:
    """
    class Meta:
        name = "driversLicenseInfo"

    licenseNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    state: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    dateOfBirth: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class EcheckAccountInfoType:
    """
    :ivar accType:
    :ivar accNum:
    :ivar routingNum:
    """
    class Meta:
        name = "echeckAccountInfoType"

    accType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    accNum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    routingNum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class EcheckForTokenType:
    """
    :ivar accNum:
    :ivar routingNum:
    """
    class Meta:
        name = "echeckForTokenType"

    accNum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    routingNum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class EcheckTokenInfoType:
    """
    :ivar accType:
    :ivar cnpToken:
    :ivar routingNum:
    """
    class Meta:
        name = "echeckTokenInfoType"

    accType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    cnpToken: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    routingNum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class EcheckTokenType:
    """
    :ivar cnpToken:
    :ivar routingNum:
    :ivar accType:
    :ivar checkNum:
    """
    class Meta:
        name = "echeckTokenType"

    cnpToken: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    routingNum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    accType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    checkNum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class EcheckType:
    """
    :ivar accType:
    :ivar accNum:
    :ivar routingNum:
    :ivar checkNum:
    :ivar ccdPaymentInformation:
    """
    class Meta:
        name = "echeckType"

    accType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    accNum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    routingNum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    checkNum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    ccdPaymentInformation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class ExtendedCardResponseType:
    """
    :ivar message:
    :ivar code:
    """
    class Meta:
        name = "extendedCardResponseType"

    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class FilteringType:
    """
    :ivar prepaid:
    :ivar international:
    :ivar chargeback:
    """
    class Meta:
        name = "filteringType"

    prepaid: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    international: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    chargeback: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class FraudCheckType:
    """
    :ivar authenticationValue:
    :ivar authenticationTransactionId:
    :ivar customerIpAddress:
    :ivar authenticatedByMerchant:
    :ivar authenticationProtocolVersion:
    :ivar tokenAuthenticationValue:
    """
    class Meta:
        name = "fraudCheckType"

    authenticationValue: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    authenticationTransactionId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    customerIpAddress: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    authenticatedByMerchant: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    authenticationProtocolVersion: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    tokenAuthenticationValue: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class GiftCardCardType:
    """
    :ivar type:
    :ivar number:
    :ivar expDate:
    :ivar track:
    :ivar cardValidationNum:
    :ivar pin:
    """
    class Meta:
        name = "giftCardCardType"

    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    expDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    track: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    cardValidationNum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    pin: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class GiftCardResponse:
    """
    :ivar txnTime:
    :ivar refCode:
    :ivar systemTraceId:
    :ivar sequenceNumber:
    :ivar availableBalance:
    :ivar beginningBalance:
    :ivar endingBalance:
    :ivar cashBackAmount:
    """
    class Meta:
        name = "giftCardResponse"
        namespace = "http://www.vantivcnp.com/schema"

    txnTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    refCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    systemTraceId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    sequenceNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    availableBalance: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    beginningBalance: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    endingBalance: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    cashBackAmount: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class GiropayResponse:
    """
    :ivar redirectUrl:
    :ivar redirectToken:
    :ivar paymentPurpose:
    """
    class Meta:
        name = "giropayResponse"
        namespace = "http://www.vantivcnp.com/schema"

    redirectUrl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    redirectToken: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    paymentPurpose: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class GiropayType:
    """
    :ivar preferredLanguage:
    """
    class Meta:
        name = "giropayType"

    preferredLanguage: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class HealthcareAmounts:
    """
    :ivar totalHealthcareAmount:
    :ivar rxAmount:
    :ivar visionAmount:
    :ivar clinicOtherAmount:
    :ivar dentalAmount:
    :ivar copayAmount:
    """
    class Meta:
        name = "healthcareAmounts"
        namespace = "http://www.vantivcnp.com/schema"

    totalHealthcareAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    rxAmount: Optional[int] = field(
        default=None,
        metadata={
            "name": "RxAmount",
            "type": "Element",
        }
    )
    visionAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    clinicOtherAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    dentalAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    copayAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class IdealResponse:
    """
    :ivar redirectUrl:
    :ivar redirectToken:
    :ivar paymentPurpose:
    """
    class Meta:
        name = "idealResponse"
        namespace = "http://www.vantivcnp.com/schema"

    redirectUrl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    redirectToken: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    paymentPurpose: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class IdealType:
    """
    :ivar preferredLanguage:
    """
    class Meta:
        name = "idealType"

    preferredLanguage: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class LodgingCharge:
    """
    :ivar name:
    """
    class Meta:
        name = "lodgingCharge"
        namespace = "http://www.vantivcnp.com/schema"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class MerchantDataType:
    """
    :ivar campaign:
    :ivar affiliate:
    :ivar merchantGroupingId:
    """
    class Meta:
        name = "merchantDataType"

    campaign: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    affiliate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    merchantGroupingId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class MposType:
    """
    :ivar ksn:
    :ivar formatId:
    :ivar encryptedTrack:
    :ivar track1Status:
    :ivar track2Status:
    """
    class Meta:
        name = "mposType"

    ksn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    formatId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    encryptedTrack: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    track1Status: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    track2Status: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class NetworkSubField:
    """
    :ivar fieldValue:
    :ivar fieldNumber:
    """
    class Meta:
        name = "networkSubField"

    fieldValue: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    fieldNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PayPal:
    """
    :ivar payerEmail:
    :ivar payerId:
    :ivar token:
    :ivar transactionId:
    """
    class Meta:
        name = "payPal"

    payerEmail: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    payerId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    token: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    transactionId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class PinlessDebitResponse:
    """
    :ivar networkName:
    :ivar debitResponse:
    :ivar debitMessage:
    """
    class Meta:
        name = "pinlessDebitResponse"
        namespace = "http://www.vantivcnp.com/schema"

    networkName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    debitResponse: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    debitMessage: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Pos:
    """
    :ivar capability:
    :ivar entryMode:
    :ivar cardholderId:
    :ivar terminalId:
    :ivar catLevel:
    """
    class Meta:
        name = "pos"
        namespace = "http://www.vantivcnp.com/schema"

    capability: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    entryMode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    cardholderId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    terminalId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    catLevel: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class PreferredDebitNetworksType:
    """
    :ivar debitNetworkName:
    """
    class Meta:
        name = "preferredDebitNetworksType"

    debitNetworkName: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
            "max_occurs": 12,
        }
    )


@dataclass
class ProcessingInstructions:
    """
    :ivar bypassVelocityCheck:
    """
    class Meta:
        name = "processingInstructions"
        namespace = "http://www.vantivcnp.com/schema"

    bypassVelocityCheck: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class RecurringResponseType:
    """
    :ivar subscriptionId:
    :ivar responseCode:
    :ivar responseMessage:
    :ivar recurringTxnId:
    """
    class Meta:
        name = "recurringResponseType"

    subscriptionId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    responseCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    responseMessage: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    recurringTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class RecycleAdviceType:
    """
    :ivar nextRecycleTime:
    :ivar recycleAdviceEnd:
    """
    class Meta:
        name = "recycleAdviceType"

    nextRecycleTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    recycleAdviceEnd: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class RecyclingRequestType:
    """
    :ivar recycleBy:
    :ivar recycleId:
    """
    class Meta:
        name = "recyclingRequestType"

    recycleBy: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    recycleId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class SepaDirectDebitResponse:
    """
    :ivar redirectUrl:
    :ivar redirectToken:
    :ivar mandateReference:
    """
    class Meta:
        name = "sepaDirectDebitResponse"
        namespace = "http://www.vantivcnp.com/schema"

    redirectUrl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    redirectToken: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    mandateReference: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class SepaDirectDebitType:
    """
    :ivar mandateProvider:
    :ivar sequenceType:
    :ivar mandateReference:
    :ivar mandateUrl:
    :ivar mandateSignatureDate:
    :ivar iban:
    :ivar preferredLanguage:
    """
    class Meta:
        name = "sepaDirectDebitType"

    mandateProvider: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    sequenceType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    mandateReference: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    mandateUrl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    mandateSignatureDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    iban: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    preferredLanguage: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class SofortResponse:
    """
    :ivar redirectUrl:
    :ivar redirectToken:
    :ivar paymentPurpose:
    """
    class Meta:
        name = "sofortResponse"
        namespace = "http://www.vantivcnp.com/schema"

    redirectUrl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    redirectToken: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    paymentPurpose: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class SofortType:
    """
    :ivar preferredLanguage:
    """
    class Meta:
        name = "sofortType"

    preferredLanguage: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class TokenResponseType:
    """
    :ivar cnpToken:
    :ivar tokenResponseCode:
    :ivar tokenMessage:
    :ivar type:
    :ivar bin:
    :ivar eCheckAccountSuffix:
    """
    class Meta:
        name = "tokenResponseType"

    cnpToken: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    tokenResponseCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    tokenMessage: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    bin: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    eCheckAccountSuffix: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class TransactionReversalRecyclingResponseType:
    """
    :ivar creditCnpTxnId:
    """
    class Meta:
        name = "transactionReversalRecyclingResponseType"

    creditCnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class UpdateAddOnType:
    """
    :ivar addOnCode:
    :ivar name:
    :ivar amount:
    :ivar startDate:
    :ivar endDate:
    """
    class Meta:
        name = "updateAddOnType"

    addOnCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    startDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    endDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class UpdateCardValidationNumOnToken:
    """
    :ivar orderId:
    :ivar cnpToken:
    :ivar cardValidationNum:
    """
    class Meta:
        name = "updateCardValidationNumOnToken"
        namespace = "http://www.vantivcnp.com/schema"

    orderId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    cnpToken: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    cardValidationNum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class UpdateDiscountType:
    """
    :ivar discountCode:
    :ivar name:
    :ivar amount:
    :ivar startDate:
    :ivar endDate:
    """
    class Meta:
        name = "updateDiscountType"

    discountCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    startDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    endDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class VirtualGiftCardResponse:
    """
    :ivar accountNumber:
    :ivar pin:
    """
    class Meta:
        name = "virtualGiftCardResponse"
        namespace = "http://www.vantivcnp.com/schema"

    accountNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    pin: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class VirtualGiftCardType:
    """
    :ivar accountNumberLength:
    :ivar giftCardBin:
    """
    class Meta:
        name = "virtualGiftCardType"

    accountNumberLength: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    giftCardBin: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class VoidRecyclingResponseType:
    """
    :ivar creditCnpTxnId:
    """
    class Meta:
        name = "voidRecyclingResponseType"

    creditCnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class Wallet:
    """
    :ivar walletSourceType:
    :ivar walletSourceTypeId:
    """
    class Meta:
        name = "wallet"
        namespace = "http://www.vantivcnp.com/schema"

    walletSourceType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    walletSourceTypeId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class RFRRequest:
    """
    :ivar cnpSessionId:
    :ivar accountUpdateFileRequestData:
    """
    class Meta:
        namespace = "http://www.vantivcnp.com/schema"

    cnpSessionId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    accountUpdateFileRequestData: Optional[AccountUpdateFileRequestData] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class AccountUpdater:
    """
    :ivar originalAccountInfo:
    :ivar newAccountInfo:
    :ivar originalTokenInfo:
    :ivar newTokenInfo:
    :ivar originalCardInfo:
    :ivar newCardInfo:
    :ivar extendedCardResponse:
    :ivar accountUpdateSource:
    :ivar originalCardTokenInfo:
    :ivar newCardTokenInfo:
    """
    class Meta:
        name = "accountUpdater"
        namespace = "http://www.vantivcnp.com/schema"

    originalAccountInfo: Optional[EcheckAccountInfoType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    newAccountInfo: Optional[EcheckAccountInfoType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalTokenInfo: Optional[EcheckTokenInfoType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    newTokenInfo: Optional[EcheckTokenInfoType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalCardInfo: Optional[CardAccountInfoType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    newCardInfo: Optional[CardAccountInfoType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    extendedCardResponse: List[ExtendedCardResponseType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    accountUpdateSource: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    originalCardTokenInfo: Optional[CardTokenInfoType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    newCardTokenInfo: Optional[CardTokenInfoType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class ApplepayType:
    """
    :ivar data:
    :ivar header:
    :ivar signature:
    :ivar version:
    """
    class Meta:
        name = "applepayType"

    data: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    header: Optional[ApplepayHeaderType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    signature: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class BillToAddress(Contact):
    class Meta:
        name = "billToAddress"
        namespace = "http://www.vantivcnp.com/schema"


@dataclass
class Card(CardType):
    class Meta:
        name = "card"
        namespace = "http://www.vantivcnp.com/schema"


@dataclass
class CardTokenTypeAu(CardTokenType):
    """
    :ivar bin:
    """
    class Meta:
        name = "cardTokenTypeAU"

    bin: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class EcheckTypeCtx:
    """
    :ivar accType:
    :ivar accNum:
    :ivar routingNum:
    :ivar checkNum:
    :ivar ccdPaymentInformation:
    :ivar ctxPaymentInformation:
    """
    class Meta:
        name = "echeckTypeCtx"

    accType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    accNum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    routingNum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    checkNum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    ccdPaymentInformation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    ctxPaymentInformation: Optional[CtxPaymentInformationType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class FraudResult:
    """
    :ivar avsResult:
    :ivar cardValidationResult:
    :ivar authenticationResult:
    :ivar advancedAvsresult:
    :ivar advancedFraudResults:
    """
    class Meta:
        name = "fraudResult"
        namespace = "http://www.vantivcnp.com/schema"

    avsResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    cardValidationResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    authenticationResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    advancedAvsresult: Optional[str] = field(
        default=None,
        metadata={
            "name": "advancedAVSResult",
            "type": "Element",
        }
    )
    advancedFraudResults: Optional[AdvancedFraudResultsType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class HealthcareIias:
    """
    :ivar healthcareAmounts:
    :ivar iiasflag:
    """
    class Meta:
        name = "healthcareIIAS"
        namespace = "http://www.vantivcnp.com/schema"

    healthcareAmounts: Optional[HealthcareAmounts] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    iiasflag: Optional[str] = field(
        default=None,
        metadata={
            "name": "IIASFlag",
            "type": "Element",
        }
    )


@dataclass
class LineItemData:
    """
    :ivar itemSequenceNumber:
    :ivar itemDescription:
    :ivar productCode:
    :ivar quantity:
    :ivar unitOfMeasure:
    :ivar taxAmount:
    :ivar lineItemTotal:
    :ivar lineItemTotalWithTax:
    :ivar itemDiscountAmount:
    :ivar commodityCode:
    :ivar unitCost:
    :ivar detailTax:
    """
    class Meta:
        name = "lineItemData"
        namespace = "http://www.vantivcnp.com/schema"

    itemSequenceNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    itemDescription: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    productCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    unitOfMeasure: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    taxAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    lineItemTotal: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    lineItemTotalWithTax: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    itemDiscountAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    commodityCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    unitCost: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    detailTax: List[DetailTax] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 6,
        }
    )


@dataclass
class LodgingInfo:
    """
    :ivar hotelFolioNumber:
    :ivar checkInDate:
    :ivar checkOutDate:
    :ivar duration:
    :ivar customerServicePhone:
    :ivar programCode:
    :ivar roomRate:
    :ivar roomTax:
    :ivar numAdults:
    :ivar propertyLocalPhone:
    :ivar fireSafetyIndicator:
    :ivar lodgingCharge:
    """
    class Meta:
        name = "lodgingInfo"
        namespace = "http://www.vantivcnp.com/schema"

    hotelFolioNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    checkInDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    checkOutDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    duration: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    customerServicePhone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    programCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    roomRate: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    roomTax: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    numAdults: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    propertyLocalPhone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fireSafetyIndicator: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    lodgingCharge: List[LodgingCharge] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 6,
        }
    )


@dataclass
class NetworkField:
    """
    :ivar fieldValue:
    :ivar networkSubField:
    :ivar fieldNumber:
    :ivar fieldName:
    """
    class Meta:
        name = "networkField"

    fieldValue: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    networkSubField: List[NetworkSubField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    fieldNumber: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    fieldName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PinlessDebitRequestType:
    """
    :ivar routingPreference:
    :ivar preferredDebitNetworks:
    """
    class Meta:
        name = "pinlessDebitRequestType"

    routingPreference: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    preferredDebitNetworks: Optional[PreferredDebitNetworksType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class RecurringSubscriptionType:
    """
    :ivar planCode:
    :ivar numberOfPayments:
    :ivar startDate:
    :ivar amount:
    :ivar createDiscount:
    :ivar createAddOn:
    """
    class Meta:
        name = "recurringSubscriptionType"

    planCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    numberOfPayments: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    startDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    createDiscount: List[CreateDiscountType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    createAddOn: List[CreateAddOnType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class RecurringTransactionResponseType(CnpTransactionInterface):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar message:
    :ivar responseTime:
    :ivar location:
    """
    class Meta:
        name = "recurringTransactionResponseType"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class RecurringTransactionType(CnpTransactionInterface):
    class Meta:
        name = "recurringTransactionType"


@dataclass
class RecyclingResponseType:
    """
    :ivar recycleAdvice:
    :ivar recycleEngineActive:
    """
    class Meta:
        name = "recyclingResponseType"

    recycleAdvice: Optional[RecycleAdviceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    recycleEngineActive: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class ShipToAddress(Contact):
    class Meta:
        name = "shipToAddress"
        namespace = "http://www.vantivcnp.com/schema"


@dataclass
class Token(CardTokenType):
    class Meta:
        name = "token"
        namespace = "http://www.vantivcnp.com/schema"


@dataclass
class TransactionType(CnpTransactionInterface):
    """
    :ivar id:
    :ivar customerId:
    """
    class Meta:
        name = "transactionType"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    customerId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class AuthInformation:
    """
    :ivar authDate:
    :ivar authCode:
    :ivar fraudResult:
    :ivar authAmount:
    """
    class Meta:
        name = "authInformation"
        namespace = "http://www.vantivcnp.com/schema"

    authDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    authCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fraudResult: Optional[FraudResult] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    authAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class CancelSubscription(RecurringTransactionType):
    """
    :ivar subscriptionId:
    """
    class Meta:
        name = "cancelSubscription"
        namespace = "http://www.vantivcnp.com/schema"

    subscriptionId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class CancelSubscriptionResponse(RecurringTransactionResponseType):
    """
    :ivar subscriptionId:
    """
    class Meta:
        name = "cancelSubscriptionResponse"
        namespace = "http://www.vantivcnp.com/schema"

    subscriptionId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class CreatePlan(RecurringTransactionType):
    """
    :ivar planCode:
    :ivar name:
    :ivar description:
    :ivar intervalType:
    :ivar amount:
    :ivar numberOfPayments:
    :ivar trialNumberOfIntervals:
    :ivar trialIntervalType:
    :ivar active:
    """
    class Meta:
        name = "createPlan"
        namespace = "http://www.vantivcnp.com/schema"

    planCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    intervalType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    numberOfPayments: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    trialNumberOfIntervals: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    trialIntervalType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    active: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class CreatePlanResponse(RecurringTransactionResponseType):
    """
    :ivar planCode:
    """
    class Meta:
        name = "createPlanResponse"
        namespace = "http://www.vantivcnp.com/schema"

    planCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class EnhancedData:
    """
    :ivar customerReference:
    :ivar salesTax:
    :ivar deliveryType:
    :ivar taxExempt:
    :ivar discountAmount:
    :ivar shippingAmount:
    :ivar dutyAmount:
    :ivar shipFromPostalCode:
    :ivar destinationPostalCode:
    :ivar destinationCountryCode:
    :ivar invoiceReferenceNumber:
    :ivar orderDate:
    :ivar detailTax:
    :ivar lineItemData:
    """
    class Meta:
        name = "enhancedData"
        namespace = "http://www.vantivcnp.com/schema"

    customerReference: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    salesTax: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    deliveryType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    taxExempt: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    discountAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    shippingAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    dutyAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    shipFromPostalCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    destinationPostalCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    destinationCountryCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    invoiceReferenceNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    orderDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    detailTax: List[DetailTax] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 6,
        }
    )
    lineItemData: List[LineItemData] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 99,
        }
    )


@dataclass
class NetworkResponse:
    """
    :ivar endpoint:
    :ivar networkField:
    """
    class Meta:
        name = "networkResponse"

    endpoint: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    networkField: List[NetworkField] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class RecurringRequestType:
    """
    :ivar createSubscription:
    """
    class Meta:
        name = "recurringRequestType"

    createSubscription: Optional[RecurringSubscriptionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class RecurringTransaction(RecurringTransactionType):
    class Meta:
        name = "recurringTransaction"
        namespace = "http://www.vantivcnp.com/schema"


@dataclass
class RecurringTransactionResponse(RecurringTransactionResponseType):
    class Meta:
        name = "recurringTransactionResponse"
        namespace = "http://www.vantivcnp.com/schema"


@dataclass
class Transaction(TransactionType):
    class Meta:
        name = "transaction"
        namespace = "http://www.vantivcnp.com/schema"


@dataclass
class TransactionTypeOptionReportGroup(TransactionType):
    """
    :ivar reportGroup:
    """
    class Meta:
        name = "transactionTypeOptionReportGroup"

    reportGroup: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TransactionTypeWithReportGroup(TransactionType):
    """
    :ivar reportGroup:
    """
    class Meta:
        name = "transactionTypeWithReportGroup"

    reportGroup: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TransactionTypeWithReportGroupAndPartial(TransactionType):
    """
    :ivar reportGroup:
    :ivar partial:
    """
    class Meta:
        name = "transactionTypeWithReportGroupAndPartial"

    reportGroup: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    partial: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class UpdatePlan(RecurringTransactionType):
    """
    :ivar planCode:
    :ivar active:
    """
    class Meta:
        name = "updatePlan"
        namespace = "http://www.vantivcnp.com/schema"

    planCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    active: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class UpdatePlanResponse(RecurringTransactionResponseType):
    """
    :ivar planCode:
    """
    class Meta:
        name = "updatePlanResponse"
        namespace = "http://www.vantivcnp.com/schema"

    planCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class UpdateSubscription(RecurringTransactionType):
    """
    :ivar subscriptionId:
    :ivar planCode:
    :ivar billToAddress:
    :ivar card:
    :ivar token:
    :ivar paypage:
    :ivar billingDate:
    :ivar createDiscount:
    :ivar updateDiscount:
    :ivar deleteDiscount:
    :ivar createAddOn:
    :ivar updateAddOn:
    :ivar deleteAddOn:
    """
    class Meta:
        name = "updateSubscription"
        namespace = "http://www.vantivcnp.com/schema"

    subscriptionId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    planCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    billToAddress: Optional[BillToAddress] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    card: Optional[CardType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    token: Optional[CardTokenType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    paypage: Optional[CardPaypageType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    billingDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    createDiscount: List[CreateDiscountType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    updateDiscount: List[UpdateDiscountType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    deleteDiscount: List[DeleteDiscountType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    createAddOn: List[CreateAddOnType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    updateAddOn: List[UpdateAddOnType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    deleteAddOn: List[DeleteAddOnType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class UpdateSubscriptionResponse(RecurringTransactionResponseType):
    """
    :ivar subscriptionId:
    :ivar tokenResponse:
    """
    class Meta:
        name = "updateSubscriptionResponse"
        namespace = "http://www.vantivcnp.com/schema"

    subscriptionId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    tokenResponse: Optional[TokenResponseType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class AccountUpdate(TransactionTypeWithReportGroup):
    """
    :ivar orderId:
    :ivar token:
    :ivar card:
    :ivar cardOrToken:
    """
    class Meta:
        name = "accountUpdate"
        namespace = "http://www.vantivcnp.com/schema"

    orderId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    token: Optional[Token] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    card: Optional[Card] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    cardOrToken: Optional[CardOrToken] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class AccountUpdateResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar orderId:
    :ivar response:
    :ivar responseTime:
    :ivar message:
    :ivar updatedCard:
    :ivar originalCard:
    :ivar updatedToken:
    :ivar originalToken:
    """
    class Meta:
        name = "accountUpdateResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    orderId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    updatedCard: Optional[CardType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalCard: Optional[CardType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    updatedToken: Optional[CardTokenTypeAu] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalToken: Optional[CardTokenTypeAu] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Activate(TransactionTypeWithReportGroup):
    """
    :ivar orderId:
    :ivar amount:
    :ivar orderSource:
    :ivar card:
    :ivar virtualGiftCard:
    """
    class Meta:
        name = "activate"
        namespace = "http://www.vantivcnp.com/schema"

    orderId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    orderSource: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    card: Optional[GiftCardCardType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    virtualGiftCard: Optional[VirtualGiftCardType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class ActivateResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar fraudResult:
    :ivar giftCardResponse:
    :ivar virtualGiftCardResponse:
    """
    class Meta:
        name = "activateResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fraudResult: Optional[FraudResult] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    giftCardResponse: Optional[GiftCardResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    virtualGiftCardResponse: Optional[VirtualGiftCardResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class ActivateReversal(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar card:
    :ivar virtualGiftCardBin:
    :ivar originalRefCode:
    :ivar originalAmount:
    :ivar originalTxnTime:
    :ivar originalSystemTraceId:
    :ivar originalSequenceNumber:
    """
    class Meta:
        name = "activateReversal"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    card: Optional[GiftCardCardType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    virtualGiftCardBin: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalRefCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalTxnTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalSystemTraceId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalSequenceNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class ActivateReversalResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar giftCardResponse:
    """
    class Meta:
        name = "activateReversalResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    giftCardResponse: Optional[GiftCardResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class AuthReversal(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar amount:
    :ivar surchargeAmount:
    :ivar payPalNotes:
    :ivar actionReason:
    """
    class Meta:
        name = "authReversal"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    surchargeAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    payPalNotes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    actionReason: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class AuthReversalResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar pinlessDebitResponse:
    """
    class Meta:
        name = "authReversalResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    pinlessDebitResponse: Optional[PinlessDebitResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Authorization(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar orderId:
    :ivar amount:
    :ivar secondaryAmount:
    :ivar surchargeAmount:
    :ivar orderSource:
    :ivar customerInfo:
    :ivar billToAddress:
    :ivar shipToAddress:
    :ivar mpos:
    :ivar card:
    :ivar paypal:
    :ivar token:
    :ivar paypage:
    :ivar applepay:
    :ivar cardholderAuthentication:
    :ivar processingInstructions:
    :ivar pos:
    :ivar customBilling:
    :ivar taxType:
    :ivar enhancedData:
    :ivar allowPartialAuth:
    :ivar healthcareIias:
    :ivar lodgingInfo:
    :ivar filtering:
    :ivar merchantData:
    :ivar recyclingRequest:
    :ivar fraudFilterOverride:
    :ivar recurringRequest:
    :ivar debtRepayment:
    :ivar advancedFraudChecks:
    :ivar wallet:
    :ivar processingType:
    :ivar originalNetworkTransactionId:
    :ivar originalTransactionAmount:
    :ivar pinlessDebitRequest:
    :ivar skipRealtimeAu:
    :ivar merchantCategoryCode:
    :ivar businessIndicator:
    """
    class Meta:
        name = "authorization"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    orderId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    secondaryAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    surchargeAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    orderSource: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    customerInfo: Optional[CustomerInfo] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    billToAddress: Optional[BillToAddress] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    shipToAddress: Optional[ShipToAddress] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    mpos: Optional[MposType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    card: Optional[CardType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    paypal: Optional[PayPal] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    token: Optional[CardTokenType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    paypage: Optional[CardPaypageType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    applepay: Optional[ApplepayType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    cardholderAuthentication: Optional[FraudCheckType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    processingInstructions: Optional[ProcessingInstructions] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    pos: Optional[Pos] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    customBilling: Optional[CustomBilling] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    taxType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    enhancedData: Optional[EnhancedData] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    allowPartialAuth: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    healthcareIias: Optional[HealthcareIias] = field(
        default=None,
        metadata={
            "name": "healthcareIIAS",
            "type": "Element",
        }
    )
    lodgingInfo: Optional[LodgingInfo] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    filtering: Optional[FilteringType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    merchantData: Optional[MerchantDataType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    recyclingRequest: Optional[RecyclingRequestType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fraudFilterOverride: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    recurringRequest: Optional[RecurringRequestType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    debtRepayment: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    advancedFraudChecks: Optional[AdvancedFraudChecksType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    wallet: Optional[Wallet] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    processingType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalNetworkTransactionId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalTransactionAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    pinlessDebitRequest: Optional[PinlessDebitRequestType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    skipRealtimeAu: Optional[bool] = field(
        default=None,
        metadata={
            "name": "skipRealtimeAU",
            "type": "Element",
        }
    )
    merchantCategoryCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    businessIndicator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class BalanceInquiry(TransactionTypeWithReportGroup):
    """
    :ivar orderId:
    :ivar orderSource:
    :ivar card:
    """
    class Meta:
        name = "balanceInquiry"
        namespace = "http://www.vantivcnp.com/schema"

    orderId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    orderSource: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    card: Optional[GiftCardCardType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class BalanceInquiryResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar fraudResult:
    :ivar giftCardResponse:
    """
    class Meta:
        name = "balanceInquiryResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fraudResult: Optional[FraudResult] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    giftCardResponse: Optional[GiftCardResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Capture(TransactionTypeWithReportGroupAndPartial):
    """
    :ivar cnpTxnId:
    :ivar amount:
    :ivar surchargeAmount:
    :ivar enhancedData:
    :ivar processingInstructions:
    :ivar payPalOrderComplete:
    :ivar payPalNotes:
    :ivar customBilling:
    :ivar lodgingInfo:
    :ivar pin:
    """
    class Meta:
        name = "capture"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    surchargeAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    enhancedData: Optional[EnhancedData] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    processingInstructions: Optional[ProcessingInstructions] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    payPalOrderComplete: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    payPalNotes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    customBilling: Optional[CustomBilling] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    lodgingInfo: Optional[LodgingInfo] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    pin: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class CaptureGivenAuth(TransactionTypeWithReportGroup):
    """
    :ivar orderId:
    :ivar authInformation:
    :ivar amount:
    :ivar secondaryAmount:
    :ivar surchargeAmount:
    :ivar orderSource:
    :ivar billToAddress:
    :ivar shipToAddress:
    :ivar mpos:
    :ivar card:
    :ivar token:
    :ivar paypage:
    :ivar customBilling:
    :ivar taxType:
    :ivar enhancedData:
    :ivar lodgingInfo:
    :ivar processingInstructions:
    :ivar pos:
    :ivar merchantData:
    :ivar debtRepayment:
    :ivar processingType:
    :ivar originalNetworkTransactionId:
    :ivar originalTransactionAmount:
    :ivar merchantCategoryCode:
    :ivar businessIndicator:
    """
    class Meta:
        name = "captureGivenAuth"
        namespace = "http://www.vantivcnp.com/schema"

    orderId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    authInformation: Optional[AuthInformation] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    secondaryAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    surchargeAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    orderSource: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    billToAddress: Optional[BillToAddress] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    shipToAddress: Optional[ShipToAddress] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    mpos: Optional[MposType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    card: Optional[CardType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    token: Optional[CardTokenType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    paypage: Optional[CardPaypageType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    customBilling: Optional[CustomBilling] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    taxType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    enhancedData: Optional[EnhancedData] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    lodgingInfo: Optional[LodgingInfo] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    processingInstructions: Optional[ProcessingInstructions] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    pos: Optional[Pos] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    merchantData: Optional[MerchantDataType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    debtRepayment: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    processingType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalNetworkTransactionId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalTransactionAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    merchantCategoryCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    businessIndicator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class CaptureGivenAuthResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar tokenResponse:
    :ivar fraudResult:
    :ivar giftCardResponse:
    """
    class Meta:
        name = "captureGivenAuthResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    tokenResponse: Optional[TokenResponseType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fraudResult: Optional[FraudResult] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    giftCardResponse: Optional[GiftCardResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class CaptureResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar accountUpdater:
    :ivar fraudResult:
    :ivar pinlessDebitResponse:
    """
    class Meta:
        name = "captureResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    accountUpdater: Optional[AccountUpdater] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fraudResult: Optional[FraudResult] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    pinlessDebitResponse: Optional[PinlessDebitResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Credit(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar amount:
    :ivar secondaryAmount:
    :ivar surchargeAmount:
    :ivar customBilling:
    :ivar enhancedData:
    :ivar lodgingInfo:
    :ivar processingInstructions:
    :ivar pos:
    :ivar pin:
    :ivar orderId:
    :ivar orderSource:
    :ivar billToAddress:
    :ivar mpos:
    :ivar card:
    :ivar token:
    :ivar paypage:
    :ivar paypal:
    :ivar taxType:
    :ivar merchantData:
    :ivar merchantCategoryCode:
    :ivar payPalNotes:
    :ivar actionReason:
    :ivar businessIndicator:
    """
    class Meta:
        name = "credit"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    amount: List[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    secondaryAmount: List[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    surchargeAmount: List[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    customBilling: List[CustomBilling] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    enhancedData: List[EnhancedData] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    lodgingInfo: List[LodgingInfo] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    processingInstructions: List[ProcessingInstructions] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    pin: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    orderId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    orderSource: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    billToAddress: Optional[BillToAddress] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    mpos: Optional[MposType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    card: Optional[CardType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    token: Optional[CardTokenType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    paypage: Optional[CardPaypageType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    paypal: Optional[PayPal] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    taxType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    merchantData: Optional[MerchantDataType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    merchantCategoryCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    payPalNotes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    actionReason: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    businessIndicator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class CreditResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar tokenResponse:
    :ivar fraudResult:
    """
    class Meta:
        name = "creditResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    tokenResponse: Optional[TokenResponseType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fraudResult: Optional[FraudResult] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class CustomerCredit(TransactionTypeWithReportGroup):
    """
    :ivar fundingCustomerId:
    :ivar customerName:
    :ivar fundsTransferId:
    :ivar amount:
    :ivar accountInfo:
    :ivar customIdentifier:
    """
    class Meta:
        name = "customerCredit"
        namespace = "http://www.vantivcnp.com/schema"

    fundingCustomerId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    customerName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundsTransferId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    accountInfo: Optional[EcheckTypeCtx] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    customIdentifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class CustomerCreditResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar fundsTransferId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar duplicate:
    """
    class Meta:
        name = "customerCreditResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundsTransferId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    duplicate: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class CustomerDebit(TransactionTypeWithReportGroup):
    """
    :ivar fundingCustomerId:
    :ivar customerName:
    :ivar fundsTransferId:
    :ivar amount:
    :ivar accountInfo:
    :ivar customIdentifier:
    """
    class Meta:
        name = "customerDebit"
        namespace = "http://www.vantivcnp.com/schema"

    fundingCustomerId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    customerName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundsTransferId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    accountInfo: Optional[EcheckTypeCtx] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    customIdentifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class CustomerDebitResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar fundsTransferId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar duplicate:
    """
    class Meta:
        name = "customerDebitResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundsTransferId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    duplicate: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Deactivate(TransactionTypeWithReportGroup):
    """
    :ivar orderId:
    :ivar orderSource:
    :ivar card:
    """
    class Meta:
        name = "deactivate"
        namespace = "http://www.vantivcnp.com/schema"

    orderId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    orderSource: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    card: Optional[GiftCardCardType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class DeactivateResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar fraudResult:
    :ivar approvedAmount:
    :ivar giftCardResponse:
    """
    class Meta:
        name = "deactivateResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fraudResult: Optional[FraudResult] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    approvedAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    giftCardResponse: Optional[GiftCardResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class DeactivateReversal(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar card:
    :ivar originalRefCode:
    :ivar originalTxnTime:
    :ivar originalSystemTraceId:
    :ivar originalSequenceNumber:
    """
    class Meta:
        name = "deactivateReversal"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    card: Optional[GiftCardCardType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalRefCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalTxnTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalSystemTraceId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalSequenceNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class DeactivateReversalResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar giftCardResponse:
    """
    class Meta:
        name = "deactivateReversalResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    giftCardResponse: Optional[GiftCardResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class DepositReversal(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar card:
    :ivar originalRefCode:
    :ivar originalAmount:
    :ivar originalTxnTime:
    :ivar originalSystemTraceId:
    :ivar originalSequenceNumber:
    """
    class Meta:
        name = "depositReversal"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    card: Optional[GiftCardCardType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalRefCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalTxnTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalSystemTraceId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalSequenceNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class DepositReversalResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar giftCardResponse:
    """
    class Meta:
        name = "depositReversalResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    giftCardResponse: Optional[GiftCardResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class EcheckCredit(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar amount:
    :ivar secondaryAmount:
    :ivar customBilling:
    :ivar customIdentifier:
    :ivar orderId:
    :ivar orderSource:
    :ivar billToAddress:
    :ivar echeck:
    :ivar echeckToken:
    :ivar merchantData:
    """
    class Meta:
        name = "echeckCredit"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    amount: List[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    secondaryAmount: List[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    customBilling: List[CustomBilling] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    customIdentifier: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    orderId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    orderSource: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    billToAddress: Optional[BillToAddress] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    echeck: Optional[EcheckType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    echeckToken: Optional[EcheckTokenType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    merchantData: Optional[MerchantDataType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class EcheckCreditResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar responseTime:
    :ivar message:
    :ivar location:
    :ivar postDate:
    :ivar accountUpdater:
    :ivar tokenResponse:
    """
    class Meta:
        name = "echeckCreditResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    accountUpdater: Optional[AccountUpdater] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    tokenResponse: Optional[TokenResponseType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class EcheckPreNoteCredit(TransactionTypeWithReportGroup):
    """
    :ivar orderId:
    :ivar orderSource:
    :ivar billToAddress:
    :ivar echeck:
    :ivar merchantData:
    """
    class Meta:
        name = "echeckPreNoteCredit"
        namespace = "http://www.vantivcnp.com/schema"

    orderId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    orderSource: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    billToAddress: Optional[BillToAddress] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    echeck: Optional[EcheckType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    merchantData: Optional[MerchantDataType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class EcheckPreNoteCreditResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar responseTime:
    :ivar message:
    """
    class Meta:
        name = "echeckPreNoteCreditResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class EcheckPreNoteSale(TransactionTypeWithReportGroup):
    """
    :ivar orderId:
    :ivar orderSource:
    :ivar billToAddress:
    :ivar echeck:
    :ivar merchantData:
    """
    class Meta:
        name = "echeckPreNoteSale"
        namespace = "http://www.vantivcnp.com/schema"

    orderId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    orderSource: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    billToAddress: Optional[BillToAddress] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    echeck: Optional[EcheckType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    merchantData: Optional[MerchantDataType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class EcheckPreNoteSaleResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar responseTime:
    :ivar message:
    """
    class Meta:
        name = "echeckPreNoteSaleResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class EcheckRedeposit(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar echeck:
    :ivar echeckToken:
    :ivar merchantData:
    :ivar customIdentifier:
    """
    class Meta:
        name = "echeckRedeposit"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    echeck: Optional[EcheckType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    echeckToken: Optional[EcheckTokenType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    merchantData: Optional[MerchantDataType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    customIdentifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class EcheckRedepositResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar responseTime:
    :ivar message:
    :ivar location:
    :ivar postDate:
    :ivar accountUpdater:
    :ivar tokenResponse:
    """
    class Meta:
        name = "echeckRedepositResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    accountUpdater: Optional[AccountUpdater] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    tokenResponse: Optional[TokenResponseType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class EcheckSale(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar amount:
    :ivar customBilling:
    :ivar customIdentifier:
    :ivar orderId:
    :ivar verify:
    :ivar secondaryAmount:
    :ivar orderSource:
    :ivar billToAddress:
    :ivar shipToAddress:
    :ivar echeck:
    :ivar echeckToken:
    :ivar merchantData:
    """
    class Meta:
        name = "echeckSale"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    amount: List[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    customBilling: List[CustomBilling] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    customIdentifier: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    orderId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    verify: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    secondaryAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    orderSource: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    billToAddress: Optional[BillToAddress] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    shipToAddress: Optional[ShipToAddress] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    echeck: Optional[EcheckType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    echeckToken: Optional[EcheckTokenType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    merchantData: Optional[MerchantDataType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class EcheckSalesResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar responseTime:
    :ivar message:
    :ivar location:
    :ivar verificationCode:
    :ivar postDate:
    :ivar accountUpdater:
    :ivar tokenResponse:
    """
    class Meta:
        name = "echeckSalesResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    verificationCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    accountUpdater: Optional[AccountUpdater] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    tokenResponse: Optional[TokenResponseType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class EcheckVerification(TransactionTypeWithReportGroup):
    """
    :ivar orderId:
    :ivar amount:
    :ivar orderSource:
    :ivar billToAddress:
    :ivar echeck:
    :ivar echeckToken:
    :ivar merchantData:
    """
    class Meta:
        name = "echeckVerification"
        namespace = "http://www.vantivcnp.com/schema"

    orderId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    orderSource: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    billToAddress: Optional[BillToAddress] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    echeck: Optional[EcheckType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    echeckToken: Optional[EcheckTokenType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    merchantData: Optional[MerchantDataType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class EcheckVerificationResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar responseTime:
    :ivar message:
    :ivar location:
    :ivar postDate:
    :ivar tokenResponse:
    """
    class Meta:
        name = "echeckVerificationResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    tokenResponse: Optional[TokenResponseType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class EcheckVoid(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    """
    class Meta:
        name = "echeckVoid"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class EcheckVoidResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    """
    class Meta:
        name = "echeckVoidResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class EnhancedAuthResponse:
    """
    :ivar fundingSource:
    :ivar affluence:
    :ivar issuerCountry:
    :ivar cardProductType:
    :ivar virtualAccountNumber:
    :ivar networkResponse:
    :ivar accountRangeId:
    """
    class Meta:
        name = "enhancedAuthResponse"
        namespace = "http://www.vantivcnp.com/schema"

    fundingSource: Optional["EnhancedAuthResponse.FundingSource"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    affluence: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    issuerCountry: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    cardProductType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    virtualAccountNumber: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    networkResponse: Optional[NetworkResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    accountRangeId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )

    @dataclass
    class FundingSource:
        """
        :ivar type:
        :ivar availableBalance:
        :ivar reloadable:
        :ivar prepaidCardType:
        """
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        availableBalance: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        reloadable: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        prepaidCardType: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )


@dataclass
class FastAccessFunding(TransactionTypeWithReportGroup):
    """
    :ivar fundingCustomerId:
    :ivar fundingSubmerchantId:
    :ivar customerName:
    :ivar submerchantName:
    :ivar fundsTransferId:
    :ivar amount:
    :ivar disbursementType:
    :ivar card:
    :ivar token:
    :ivar paypage:
    """
    class Meta:
        name = "fastAccessFunding"
        namespace = "http://www.vantivcnp.com/schema"

    fundingCustomerId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundingSubmerchantId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    customerName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    submerchantName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundsTransferId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    disbursementType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    card: Optional[CardType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    token: Optional[CardTokenType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    paypage: Optional[CardPaypageType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class FastAccessFundingResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar fundsTransferId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar tokenResponse:
    :ivar duplicate:
    """
    class Meta:
        name = "fastAccessFundingResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundsTransferId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    tokenResponse: Optional[TokenResponseType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    duplicate: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ForceCapture(TransactionTypeWithReportGroup):
    """
    :ivar orderId:
    :ivar amount:
    :ivar secondaryAmount:
    :ivar surchargeAmount:
    :ivar orderSource:
    :ivar billToAddress:
    :ivar mpos:
    :ivar card:
    :ivar token:
    :ivar paypage:
    :ivar customBilling:
    :ivar taxType:
    :ivar enhancedData:
    :ivar lodgingInfo:
    :ivar processingInstructions:
    :ivar pos:
    :ivar merchantData:
    :ivar debtRepayment:
    :ivar processingType:
    :ivar merchantCategoryCode:
    :ivar businessIndicator:
    """
    class Meta:
        name = "forceCapture"
        namespace = "http://www.vantivcnp.com/schema"

    orderId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    secondaryAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    surchargeAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    orderSource: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    billToAddress: Optional[BillToAddress] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    mpos: Optional[MposType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    card: Optional[CardType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    token: Optional[CardTokenType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    paypage: Optional[CardPaypageType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    customBilling: Optional[CustomBilling] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    taxType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    enhancedData: Optional[EnhancedData] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    lodgingInfo: Optional[LodgingInfo] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    processingInstructions: Optional[ProcessingInstructions] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    pos: Optional[Pos] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    merchantData: Optional[MerchantDataType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    debtRepayment: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    processingType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    merchantCategoryCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    businessIndicator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class ForceCaptureResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar tokenResponse:
    :ivar accountUpdater:
    :ivar fraudResult:
    :ivar giftCardResponse:
    """
    class Meta:
        name = "forceCaptureResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    tokenResponse: Optional[TokenResponseType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    accountUpdater: Optional[AccountUpdater] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fraudResult: Optional[FraudResult] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    giftCardResponse: Optional[GiftCardResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class FraudCheck(TransactionTypeWithReportGroup):
    """
    :ivar advancedFraudChecks:
    :ivar billToAddress:
    :ivar shipToAddress:
    :ivar amount:
    :ivar eventType:
    :ivar accountLogin:
    :ivar accountPasshash:
    """
    class Meta:
        name = "fraudCheck"
        namespace = "http://www.vantivcnp.com/schema"

    advancedFraudChecks: Optional[AdvancedFraudChecksType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    billToAddress: Optional[BillToAddress] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    shipToAddress: Optional[ShipToAddress] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    eventType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    accountLogin: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    accountPasshash: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class FraudCheckResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar message:
    :ivar location:
    :ivar responseTime:
    :ivar advancedFraudResults:
    """
    class Meta:
        name = "fraudCheckResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    advancedFraudResults: Optional[AdvancedFraudResultsType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class FundingInstructionVoid(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    """
    class Meta:
        name = "fundingInstructionVoid"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class FundingInstructionVoidResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar duplicate:
    """
    class Meta:
        name = "fundingInstructionVoidResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    duplicate: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class GiftCardAuthReversal(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar card:
    :ivar originalRefCode:
    :ivar originalAmount:
    :ivar originalTxnTime:
    :ivar originalSystemTraceId:
    :ivar originalSequenceNumber:
    """
    class Meta:
        name = "giftCardAuthReversal"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    card: Optional[GiftCardCardType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalRefCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalTxnTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalSystemTraceId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalSequenceNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class GiftCardAuthReversalResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar giftCardResponse:
    """
    class Meta:
        name = "giftCardAuthReversalResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    giftCardResponse: Optional[GiftCardResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class GiftCardCapture(TransactionTypeWithReportGroupAndPartial):
    """
    :ivar cnpTxnId:
    :ivar captureAmount:
    :ivar card:
    :ivar originalRefCode:
    :ivar originalAmount:
    :ivar originalTxnTime:
    """
    class Meta:
        name = "giftCardCapture"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    captureAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    card: Optional[GiftCardCardType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalRefCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalTxnTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class GiftCardCaptureResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar fraudResult:
    :ivar giftCardResponse:
    """
    class Meta:
        name = "giftCardCaptureResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fraudResult: Optional[FraudResult] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    giftCardResponse: Optional[GiftCardResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class GiftCardCredit(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar creditAmount:
    :ivar card:
    :ivar orderId:
    :ivar orderSource:
    """
    class Meta:
        name = "giftCardCredit"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    creditAmount: List[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    card: List[GiftCardCardType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    orderId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    orderSource: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class GiftCardCreditResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar fraudResult:
    :ivar giftCardResponse:
    """
    class Meta:
        name = "giftCardCreditResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fraudResult: Optional[FraudResult] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    giftCardResponse: Optional[GiftCardResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Load(TransactionTypeWithReportGroup):
    """
    :ivar orderId:
    :ivar amount:
    :ivar orderSource:
    :ivar card:
    """
    class Meta:
        name = "load"
        namespace = "http://www.vantivcnp.com/schema"

    orderId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    orderSource: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    card: Optional[GiftCardCardType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class LoadResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar fraudResult:
    :ivar giftCardResponse:
    """
    class Meta:
        name = "loadResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fraudResult: Optional[FraudResult] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    giftCardResponse: Optional[GiftCardResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class LoadReversal(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar card:
    :ivar originalRefCode:
    :ivar originalAmount:
    :ivar originalTxnTime:
    :ivar originalSystemTraceId:
    :ivar originalSequenceNumber:
    """
    class Meta:
        name = "loadReversal"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    card: Optional[GiftCardCardType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalRefCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalTxnTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalSystemTraceId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalSequenceNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class LoadReversalResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar giftCardResponse:
    """
    class Meta:
        name = "loadReversalResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    giftCardResponse: Optional[GiftCardResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class PayFacCredit(TransactionTypeWithReportGroup):
    """
    :ivar fundingSubmerchantId:
    :ivar fundsTransferId:
    :ivar amount:
    """
    class Meta:
        name = "payFacCredit"
        namespace = "http://www.vantivcnp.com/schema"

    fundingSubmerchantId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundsTransferId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class PayFacCreditResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar fundsTransferId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar duplicate:
    """
    class Meta:
        name = "payFacCreditResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundsTransferId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    duplicate: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class PayFacDebit(TransactionTypeWithReportGroup):
    """
    :ivar fundingSubmerchantId:
    :ivar fundsTransferId:
    :ivar amount:
    """
    class Meta:
        name = "payFacDebit"
        namespace = "http://www.vantivcnp.com/schema"

    fundingSubmerchantId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundsTransferId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class PayFacDebitResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar fundsTransferId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar duplicate:
    """
    class Meta:
        name = "payFacDebitResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundsTransferId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    duplicate: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class PayoutOrgCredit(TransactionTypeWithReportGroup):
    """
    :ivar fundingCustomerId:
    :ivar fundsTransferId:
    :ivar amount:
    """
    class Meta:
        name = "payoutOrgCredit"
        namespace = "http://www.vantivcnp.com/schema"

    fundingCustomerId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundsTransferId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class PayoutOrgCreditResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar fundsTransferId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar duplicate:
    """
    class Meta:
        name = "payoutOrgCreditResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundsTransferId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    duplicate: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class PayoutOrgDebit(TransactionTypeWithReportGroup):
    """
    :ivar fundingCustomerId:
    :ivar fundsTransferId:
    :ivar amount:
    """
    class Meta:
        name = "payoutOrgDebit"
        namespace = "http://www.vantivcnp.com/schema"

    fundingCustomerId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundsTransferId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class PayoutOrgDebitResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar fundsTransferId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar duplicate:
    """
    class Meta:
        name = "payoutOrgDebitResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundsTransferId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    duplicate: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class PhysicalCheckCredit(TransactionTypeWithReportGroup):
    """
    :ivar fundingCustomerId:
    :ivar fundingSubmerchantId:
    :ivar fundsTransferId:
    :ivar amount:
    """
    class Meta:
        name = "physicalCheckCredit"
        namespace = "http://www.vantivcnp.com/schema"

    fundingCustomerId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundingSubmerchantId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundsTransferId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class PhysicalCheckCreditResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar fundsTransferId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar duplicate:
    """
    class Meta:
        name = "physicalCheckCreditResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundsTransferId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    duplicate: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class PhysicalCheckDebit(TransactionTypeWithReportGroup):
    """
    :ivar fundingCustomerId:
    :ivar fundingSubmerchantId:
    :ivar fundsTransferId:
    :ivar amount:
    """
    class Meta:
        name = "physicalCheckDebit"
        namespace = "http://www.vantivcnp.com/schema"

    fundingCustomerId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundingSubmerchantId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundsTransferId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class PhysicalCheckDebitResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar fundsTransferId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar duplicate:
    """
    class Meta:
        name = "physicalCheckDebitResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundsTransferId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    duplicate: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class QueryTransaction(TransactionTypeWithReportGroup):
    """
    :ivar origId:
    :ivar origActionType:
    :ivar origCnpTxnId:
    :ivar showStatusOnly:
    """
    class Meta:
        name = "queryTransaction"
        namespace = "http://www.vantivcnp.com/schema"

    origId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    origActionType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    origCnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    showStatusOnly: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class QueryTransactionUnavailableResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar message:
    :ivar location:
    """
    class Meta:
        name = "queryTransactionUnavailableResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class RefundReversal(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar card:
    :ivar originalRefCode:
    :ivar originalAmount:
    :ivar originalTxnTime:
    :ivar originalSystemTraceId:
    :ivar originalSequenceNumber:
    """
    class Meta:
        name = "refundReversal"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    card: Optional[GiftCardCardType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalRefCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalTxnTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalSystemTraceId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalSequenceNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class RefundReversalResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar giftCardResponse:
    """
    class Meta:
        name = "refundReversalResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    giftCardResponse: Optional[GiftCardResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class RegisterTokenRequestType(TransactionTypeWithReportGroup):
    """
    :ivar encryptionKeyId:
    :ivar orderId:
    :ivar mpos:
    :ivar accountNumber:
    :ivar encryptedAccountNumber:
    :ivar echeckForToken:
    :ivar paypageRegistrationId:
    :ivar applepay:
    :ivar cardValidationNum:
    :ivar encryptedCardValidationNum:
    """
    class Meta:
        name = "registerTokenRequestType"

    encryptionKeyId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    orderId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    mpos: Optional[MposType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    accountNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    encryptedAccountNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    echeckForToken: Optional[EcheckForTokenType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    paypageRegistrationId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    applepay: Optional[ApplepayType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    cardValidationNum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    encryptedCardValidationNum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class RegisterTokenResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar cnpToken:
    :ivar bin:
    :ivar type:
    :ivar eCheckAccountSuffix:
    :ivar response:
    :ivar message:
    :ivar location:
    :ivar responseTime:
    :ivar applepayResponse:
    :ivar androidpayResponse:
    :ivar accountRangeId:
    """
    class Meta:
        name = "registerTokenResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    cnpToken: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    bin: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    eCheckAccountSuffix: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    applepayResponse: Optional[ApplepayResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    androidpayResponse: Optional[AndroidpayResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    accountRangeId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class ReserveCredit(TransactionTypeWithReportGroup):
    """
    :ivar fundingCustomerId:
    :ivar fundingSubmerchantId:
    :ivar fundsTransferId:
    :ivar amount:
    """
    class Meta:
        name = "reserveCredit"
        namespace = "http://www.vantivcnp.com/schema"

    fundingCustomerId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundingSubmerchantId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundsTransferId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class ReserveCreditResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar fundsTransferId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar duplicate:
    """
    class Meta:
        name = "reserveCreditResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundsTransferId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    duplicate: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ReserveDebit(TransactionTypeWithReportGroup):
    """
    :ivar fundingCustomerId:
    :ivar fundingSubmerchantId:
    :ivar fundsTransferId:
    :ivar amount:
    """
    class Meta:
        name = "reserveDebit"
        namespace = "http://www.vantivcnp.com/schema"

    fundingCustomerId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundingSubmerchantId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundsTransferId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class ReserveDebitResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar fundsTransferId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar duplicate:
    """
    class Meta:
        name = "reserveDebitResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundsTransferId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    duplicate: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Sale(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar orderId:
    :ivar amount:
    :ivar secondaryAmount:
    :ivar surchargeAmount:
    :ivar orderSource:
    :ivar customerInfo:
    :ivar billToAddress:
    :ivar shipToAddress:
    :ivar mpos:
    :ivar card:
    :ivar paypal:
    :ivar token:
    :ivar paypage:
    :ivar applepay:
    :ivar sepaDirectDebit:
    :ivar ideal:
    :ivar giropay:
    :ivar sofort:
    :ivar fraudCheck:
    :ivar cardholderAuthentication:
    :ivar customBilling:
    :ivar taxType:
    :ivar enhancedData:
    :ivar processingInstructions:
    :ivar pos:
    :ivar payPalOrderComplete:
    :ivar payPalNotes:
    :ivar allowPartialAuth:
    :ivar healthcareIias:
    :ivar lodgingInfo:
    :ivar filtering:
    :ivar merchantData:
    :ivar recyclingRequest:
    :ivar fraudFilterOverride:
    :ivar recurringRequest:
    :ivar cnpInternalRecurringRequest:
    :ivar debtRepayment:
    :ivar advancedFraudChecks:
    :ivar wallet:
    :ivar processingType:
    :ivar originalNetworkTransactionId:
    :ivar originalTransactionAmount:
    :ivar pinlessDebitRequest:
    :ivar skipRealtimeAu:
    :ivar merchantCategoryCode:
    :ivar businessIndicator:
    """
    class Meta:
        name = "sale"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    orderId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    secondaryAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    surchargeAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    orderSource: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    customerInfo: Optional[CustomerInfo] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    billToAddress: Optional[BillToAddress] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    shipToAddress: Optional[ShipToAddress] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    mpos: Optional[MposType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    card: Optional[CardType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    paypal: Optional[PayPal] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    token: Optional[CardTokenType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    paypage: Optional[CardPaypageType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    applepay: Optional[ApplepayType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    sepaDirectDebit: Optional[SepaDirectDebitType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    ideal: Optional[IdealType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    giropay: Optional[GiropayType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    sofort: Optional[SofortType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fraudCheck: Optional[FraudCheckType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    cardholderAuthentication: Optional[FraudCheckType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    customBilling: Optional[CustomBilling] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    taxType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    enhancedData: Optional[EnhancedData] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    processingInstructions: Optional[ProcessingInstructions] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    pos: Optional[Pos] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    payPalOrderComplete: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    payPalNotes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    allowPartialAuth: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    healthcareIias: Optional[HealthcareIias] = field(
        default=None,
        metadata={
            "name": "healthcareIIAS",
            "type": "Element",
        }
    )
    lodgingInfo: Optional[LodgingInfo] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    filtering: Optional[FilteringType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    merchantData: Optional[MerchantDataType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    recyclingRequest: Optional[RecyclingRequestType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fraudFilterOverride: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    recurringRequest: Optional[RecurringRequestType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    cnpInternalRecurringRequest: Optional[CnpInternalRecurringRequestType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    debtRepayment: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    advancedFraudChecks: Optional[AdvancedFraudChecksType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    wallet: Optional[Wallet] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    processingType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalNetworkTransactionId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalTransactionAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    pinlessDebitRequest: Optional[PinlessDebitRequestType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    skipRealtimeAu: Optional[bool] = field(
        default=None,
        metadata={
            "name": "skipRealtimeAU",
            "type": "Element",
        }
    )
    merchantCategoryCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    businessIndicator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class ServiceStatusRequest(TransactionTypeWithReportGroup):
    """
    :ivar serviceId:
    :ivar pathId:
    """
    class Meta:
        name = "serviceStatusRequest"
        namespace = "http://www.vantivcnp.com/schema"

    serviceId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    pathId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class ServiceStatusResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar responseTime:
    :ivar message:
    :ivar location:
    """
    class Meta:
        name = "serviceStatusResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class SubmerchantCredit(TransactionTypeWithReportGroup):
    """
    :ivar fundingSubmerchantId:
    :ivar submerchantName:
    :ivar fundsTransferId:
    :ivar amount:
    :ivar accountInfo:
    :ivar customIdentifier:
    """
    class Meta:
        name = "submerchantCredit"
        namespace = "http://www.vantivcnp.com/schema"

    fundingSubmerchantId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    submerchantName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundsTransferId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    accountInfo: Optional[EcheckTypeCtx] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    customIdentifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class SubmerchantCreditResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar fundsTransferId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar duplicate:
    """
    class Meta:
        name = "submerchantCreditResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundsTransferId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    duplicate: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class SubmerchantDebit(TransactionTypeWithReportGroup):
    """
    :ivar fundingSubmerchantId:
    :ivar submerchantName:
    :ivar fundsTransferId:
    :ivar amount:
    :ivar accountInfo:
    :ivar customIdentifier:
    """
    class Meta:
        name = "submerchantDebit"
        namespace = "http://www.vantivcnp.com/schema"

    fundingSubmerchantId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    submerchantName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundsTransferId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    accountInfo: Optional[EcheckTypeCtx] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    customIdentifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class SubmerchantDebitResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar fundsTransferId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar duplicate:
    """
    class Meta:
        name = "submerchantDebitResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundsTransferId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    duplicate: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TransactionResponse(TransactionTypeWithReportGroup):
    class Meta:
        name = "transactionResponse"
        namespace = "http://www.vantivcnp.com/schema"


@dataclass
class TransactionReversal(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar amount:
    :ivar surchargeAmount:
    :ivar enhancedData:
    :ivar processingInstructions:
    :ivar customBilling:
    :ivar lodgingInfo:
    :ivar pin:
    """
    class Meta:
        name = "transactionReversal"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    surchargeAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    enhancedData: Optional[EnhancedData] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    processingInstructions: Optional[ProcessingInstructions] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    customBilling: Optional[CustomBilling] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    lodgingInfo: Optional[LodgingInfo] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    pin: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class TransactionReversalResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar recyclingResponse:
    """
    class Meta:
        name = "transactionReversalResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    recyclingResponse: Optional[TransactionReversalRecyclingResponseType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class TranslateToLowValueTokenRequestType(TransactionTypeWithReportGroup):
    """
    :ivar orderId:
    :ivar token:
    """
    class Meta:
        name = "translateToLowValueTokenRequestType"

    orderId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    token: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )


@dataclass
class TranslateToLowValueTokenResponse(TransactionTypeWithReportGroup):
    """
    :ivar orderId:
    :ivar paypageRegistrationId:
    :ivar response:
    :ivar message:
    :ivar location:
    :ivar responseTime:
    """
    class Meta:
        name = "translateToLowValueTokenResponse"
        namespace = "http://www.vantivcnp.com/schema"

    orderId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    paypageRegistrationId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Unload(TransactionTypeWithReportGroup):
    """
    :ivar orderId:
    :ivar amount:
    :ivar orderSource:
    :ivar card:
    """
    class Meta:
        name = "unload"
        namespace = "http://www.vantivcnp.com/schema"

    orderId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    orderSource: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    card: Optional[GiftCardCardType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class UnloadResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar fraudResult:
    :ivar giftCardResponse:
    """
    class Meta:
        name = "unloadResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fraudResult: Optional[FraudResult] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    giftCardResponse: Optional[GiftCardResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class UnloadReversal(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar card:
    :ivar originalRefCode:
    :ivar originalAmount:
    :ivar originalTxnTime:
    :ivar originalSystemTraceId:
    :ivar originalSequenceNumber:
    """
    class Meta:
        name = "unloadReversal"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    card: Optional[GiftCardCardType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalRefCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalTxnTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalSystemTraceId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    originalSequenceNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class UnloadReversalResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar giftCardResponse:
    """
    class Meta:
        name = "unloadReversalResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    giftCardResponse: Optional[GiftCardResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class UpdateCardValidationNumOnTokenResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar message:
    :ivar location:
    :ivar responseTime:
    """
    class Meta:
        name = "updateCardValidationNumOnTokenResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class VendorCredit(TransactionTypeWithReportGroup):
    """
    :ivar fundingCustomerId:
    :ivar fundingSubmerchantId:
    :ivar vendorName:
    :ivar fundsTransferId:
    :ivar amount:
    :ivar accountInfo:
    """
    class Meta:
        name = "vendorCredit"
        namespace = "http://www.vantivcnp.com/schema"

    fundingCustomerId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundingSubmerchantId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    vendorName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundsTransferId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    accountInfo: Optional[EcheckTypeCtx] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class VendorCreditResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar fundsTransferId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar duplicate:
    """
    class Meta:
        name = "vendorCreditResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundsTransferId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    duplicate: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class VendorDebit(TransactionTypeWithReportGroup):
    """
    :ivar fundingCustomerId:
    :ivar fundingSubmerchantId:
    :ivar vendorName:
    :ivar fundsTransferId:
    :ivar amount:
    :ivar accountInfo:
    """
    class Meta:
        name = "vendorDebit"
        namespace = "http://www.vantivcnp.com/schema"

    fundingCustomerId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundingSubmerchantId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    vendorName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundsTransferId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    accountInfo: Optional[EcheckTypeCtx] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class VendorDebitResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar fundsTransferId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar duplicate:
    """
    class Meta:
        name = "vendorDebitResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundsTransferId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    duplicate: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Void(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar processingInstructions:
    """
    class Meta:
        name = "void"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    processingInstructions: Optional[ProcessingInstructions] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class VoidResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar responseTime:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar recyclingResponse:
    """
    class Meta:
        name = "voidResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    recyclingResponse: Optional[VoidRecyclingResponseType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class AuthorizationResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar orderId:
    :ivar response:
    :ivar responseTime:
    :ivar cardProductId:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar authCode:
    :ivar authorizationResponseSubCode:
    :ivar approvedAmount:
    :ivar accountInformation:
    :ivar accountUpdater:
    :ivar fraudResult:
    :ivar tokenResponse:
    :ivar enhancedAuthResponse:
    :ivar recyclingResponse:
    :ivar recurringResponse:
    :ivar giftCardResponse:
    :ivar applepayResponse:
    :ivar cardSuffix:
    :ivar androidpayResponse:
    :ivar networkTransactionId:
    :ivar paymentAccountReferenceNumber:
    :ivar pinlessDebitResponse:
    """
    class Meta:
        name = "authorizationResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    orderId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    cardProductId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    authCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    authorizationResponseSubCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    approvedAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    accountInformation: Optional[AccountInfoType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    accountUpdater: Optional[AccountUpdater] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fraudResult: Optional[FraudResult] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    tokenResponse: Optional[TokenResponseType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    enhancedAuthResponse: Optional[EnhancedAuthResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    recyclingResponse: Optional[RecyclingResponseType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    recurringResponse: Optional[RecurringResponseType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    giftCardResponse: Optional[GiftCardResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    applepayResponse: Optional[ApplepayResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    cardSuffix: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    androidpayResponse: Optional[AndroidpayResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    networkTransactionId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    paymentAccountReferenceNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    pinlessDebitResponse: Optional[PinlessDebitResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class RegisterTokenRequest(RegisterTokenRequestType):
    class Meta:
        name = "registerTokenRequest"
        namespace = "http://www.vantivcnp.com/schema"


@dataclass
class SaleResponse(TransactionTypeWithReportGroup):
    """
    :ivar cnpTxnId:
    :ivar response:
    :ivar orderId:
    :ivar responseTime:
    :ivar cardProductId:
    :ivar postDate:
    :ivar message:
    :ivar location:
    :ivar authCode:
    :ivar authorizationResponseSubCode:
    :ivar approvedAmount:
    :ivar accountInformation:
    :ivar fraudResult:
    :ivar tokenResponse:
    :ivar enhancedAuthResponse:
    :ivar accountUpdater:
    :ivar recyclingResponse:
    :ivar recurringResponse:
    :ivar giftCardResponse:
    :ivar applepayResponse:
    :ivar cardSuffix:
    :ivar androidpayResponse:
    :ivar sepaDirectDebitResponse:
    :ivar idealResponse:
    :ivar giropayResponse:
    :ivar sofortResponse:
    :ivar networkTransactionId:
    :ivar pinlessDebitResponse:
    :ivar paymentAccountReferenceNumber:
    """
    class Meta:
        name = "saleResponse"
        namespace = "http://www.vantivcnp.com/schema"

    cnpTxnId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    orderId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    cardProductId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    postDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    authCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    authorizationResponseSubCode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    approvedAmount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    accountInformation: Optional[AccountInfoType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fraudResult: Optional[FraudResult] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    tokenResponse: Optional[TokenResponseType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    enhancedAuthResponse: Optional[EnhancedAuthResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    accountUpdater: Optional[AccountUpdater] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    recyclingResponse: Optional[RecyclingResponseType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    recurringResponse: Optional[RecurringResponseType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    giftCardResponse: Optional[GiftCardResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    applepayResponse: Optional[ApplepayResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    cardSuffix: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    androidpayResponse: Optional[AndroidpayResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    sepaDirectDebitResponse: Optional[SepaDirectDebitResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    idealResponse: Optional[IdealResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    giropayResponse: Optional[GiropayResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    sofortResponse: Optional[SofortResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    networkTransactionId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    pinlessDebitResponse: Optional[PinlessDebitResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    paymentAccountReferenceNumber: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class TranslateToLowValueTokenRequest(TranslateToLowValueTokenRequestType):
    class Meta:
        name = "translateToLowValueTokenRequest"
        namespace = "http://www.vantivcnp.com/schema"


@dataclass
class BaseRequest:
    """
    :ivar authentication:
    :ivar serviceStatusRequest:
    :ivar queryTransaction:
    :ivar unloadReversal:
    :ivar loadReversal:
    :ivar deactivateReversal:
    :ivar activateReversal:
    :ivar refundReversal:
    :ivar depositReversal:
    :ivar echeckVoid:
    :ivar void:
    :ivar customerDebit:
    :ivar customerCredit:
    :ivar submerchantDebit:
    :ivar submerchantCredit:
    :ivar vendorDebit:
    :ivar vendorCredit:
    :ivar echeckPreNoteCredit:
    :ivar echeckPreNoteSale:
    :ivar accountUpdate:
    :ivar transactionReversal:
    :ivar translateToLowValueTokenRequest:
    :ivar payoutOrgCredit:
    :ivar payoutOrgDebit:
    :ivar fastAccessFunding:
    :ivar fundingInstructionVoid:
    :ivar physicalCheckDebit:
    :ivar physicalCheckCredit:
    :ivar reserveDebit:
    :ivar reserveCredit:
    :ivar payFacCredit:
    :ivar payFacDebit:
    :ivar fraudCheck:
    :ivar echeckRedeposit:
    :ivar echeckVerification:
    :ivar echeckCredit:
    :ivar echeckSale:
    :ivar registerTokenRequest:
    :ivar balanceInquiry:
    :ivar unload:
    :ivar load:
    :ivar deactivate:
    :ivar activate:
    :ivar giftCardCredit:
    :ivar credit:
    :ivar sale:
    :ivar captureGivenAuth:
    :ivar forceCapture:
    :ivar giftCardCapture:
    :ivar capture:
    :ivar giftCardAuthReversal:
    :ivar authReversal:
    :ivar authorization:
    :ivar updateCardValidationNumOnToken:
    :ivar transaction:
    :ivar updatePlan:
    :ivar createPlan:
    :ivar updateSubscription:
    :ivar cancelSubscription:
    :ivar recurringTransaction:
    :ivar version:
    """
    class Meta:
        name = "baseRequest"

    authentication: Optional[Authentication] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    serviceStatusRequest: Optional[ServiceStatusRequest] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    queryTransaction: Optional[QueryTransaction] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    unloadReversal: Optional[UnloadReversal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    loadReversal: Optional[LoadReversal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    deactivateReversal: Optional[DeactivateReversal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    activateReversal: Optional[ActivateReversal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    refundReversal: Optional[RefundReversal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    depositReversal: Optional[DepositReversal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    echeckVoid: Optional[EcheckVoid] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    void: Optional[Void] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    customerDebit: Optional[CustomerDebit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    customerCredit: Optional[CustomerCredit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    submerchantDebit: Optional[SubmerchantDebit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    submerchantCredit: Optional[SubmerchantCredit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    vendorDebit: Optional[VendorDebit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    vendorCredit: Optional[VendorCredit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    echeckPreNoteCredit: Optional[EcheckPreNoteCredit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    echeckPreNoteSale: Optional[EcheckPreNoteSale] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    accountUpdate: Optional[AccountUpdate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    transactionReversal: Optional[TransactionReversal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    translateToLowValueTokenRequest: Optional[TranslateToLowValueTokenRequest] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    payoutOrgCredit: Optional[PayoutOrgCredit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    payoutOrgDebit: Optional[PayoutOrgDebit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    fastAccessFunding: Optional[FastAccessFunding] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    fundingInstructionVoid: Optional[FundingInstructionVoid] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    physicalCheckDebit: Optional[PhysicalCheckDebit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    physicalCheckCredit: Optional[PhysicalCheckCredit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    reserveDebit: Optional[ReserveDebit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    reserveCredit: Optional[ReserveCredit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    payFacCredit: Optional[PayFacCredit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    payFacDebit: Optional[PayFacDebit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    fraudCheck: Optional[FraudCheck] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    echeckRedeposit: Optional[EcheckRedeposit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    echeckVerification: Optional[EcheckVerification] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    echeckCredit: Optional[EcheckCredit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    echeckSale: Optional[EcheckSale] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    registerTokenRequest: Optional[RegisterTokenRequest] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    balanceInquiry: Optional[BalanceInquiry] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    unload: Optional[Unload] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    load: Optional[Load] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    deactivate: Optional[Deactivate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    activate: Optional[Activate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    giftCardCredit: Optional[GiftCardCredit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    credit: Optional[Credit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    sale: Optional[Sale] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    captureGivenAuth: Optional[CaptureGivenAuth] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    forceCapture: Optional[ForceCapture] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    giftCardCapture: Optional[GiftCardCapture] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    capture: Optional[Capture] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    giftCardAuthReversal: Optional[GiftCardAuthReversal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    authReversal: Optional[AuthReversal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    authorization: Optional[Authorization] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    updateCardValidationNumOnToken: Optional[UpdateCardValidationNumOnToken] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    transaction: Optional[Transaction] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    updatePlan: Optional[UpdatePlan] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    createPlan: Optional[CreatePlan] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    updateSubscription: Optional[UpdateSubscription] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    cancelSubscription: Optional[CancelSubscription] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    recurringTransaction: Optional[RecurringTransaction] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.vantivcnp.com/schema",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class BatchRequest:
    """
    :ivar serviceStatusRequest:
    :ivar queryTransaction:
    :ivar unloadReversal:
    :ivar loadReversal:
    :ivar deactivateReversal:
    :ivar activateReversal:
    :ivar refundReversal:
    :ivar depositReversal:
    :ivar echeckVoid:
    :ivar void:
    :ivar customerDebit:
    :ivar customerCredit:
    :ivar submerchantDebit:
    :ivar submerchantCredit:
    :ivar vendorDebit:
    :ivar vendorCredit:
    :ivar echeckPreNoteCredit:
    :ivar echeckPreNoteSale:
    :ivar accountUpdate:
    :ivar transactionReversal:
    :ivar translateToLowValueTokenRequest:
    :ivar payoutOrgCredit:
    :ivar payoutOrgDebit:
    :ivar fastAccessFunding:
    :ivar fundingInstructionVoid:
    :ivar physicalCheckDebit:
    :ivar physicalCheckCredit:
    :ivar reserveDebit:
    :ivar reserveCredit:
    :ivar payFacCredit:
    :ivar payFacDebit:
    :ivar fraudCheck:
    :ivar echeckRedeposit:
    :ivar echeckVerification:
    :ivar echeckCredit:
    :ivar echeckSale:
    :ivar registerTokenRequest:
    :ivar balanceInquiry:
    :ivar unload:
    :ivar load:
    :ivar deactivate:
    :ivar activate:
    :ivar giftCardCredit:
    :ivar credit:
    :ivar sale:
    :ivar captureGivenAuth:
    :ivar forceCapture:
    :ivar giftCardCapture:
    :ivar capture:
    :ivar giftCardAuthReversal:
    :ivar authReversal:
    :ivar authorization:
    :ivar updateCardValidationNumOnToken:
    :ivar transaction:
    :ivar updatePlan:
    :ivar createPlan:
    :ivar updateSubscription:
    :ivar cancelSubscription:
    :ivar recurringTransaction:
    :ivar merchantSdk:
    :ivar id:
    :ivar numAuths:
    :ivar authAmount:
    :ivar numAuthReversals:
    :ivar authReversalAmount:
    :ivar numTransactionReversals:
    :ivar transactionReversalAmount:
    :ivar numGiftCardAuthReversals:
    :ivar giftCardAuthReversalOriginalAmount:
    :ivar numCaptures:
    :ivar captureAmount:
    :ivar numGiftCardCaptures:
    :ivar giftCardCaptureAmount:
    :ivar numExtCaptures:
    :ivar extCaptureAmount:
    :ivar numCredits:
    :ivar creditAmount:
    :ivar numGiftCardCredits:
    :ivar giftCardCreditAmount:
    :ivar numForceCaptures:
    :ivar forceCaptureAmount:
    :ivar numSales:
    :ivar saleAmount:
    :ivar numCaptureGivenAuths:
    :ivar captureGivenAuthAmount:
    :ivar numEcheckSales:
    :ivar echeckSalesAmount:
    :ivar numEcheckCredit:
    :ivar echeckCreditAmount:
    :ivar numEcheckVerification:
    :ivar echeckVerificationAmount:
    :ivar numEcheckRedeposit:
    :ivar numEcheckPreNoteSale:
    :ivar numEcheckPreNoteCredit:
    :ivar numAccountUpdates:
    :ivar numTokenRegistrations:
    :ivar numUpdateCardValidationNumOnTokens:
    :ivar numCancelSubscriptions:
    :ivar numUpdateSubscriptions:
    :ivar numCreatePlans:
    :ivar numUpdatePlans:
    :ivar numActivates:
    :ivar numDeactivates:
    :ivar activateAmount:
    :ivar numLoads:
    :ivar loadAmount:
    :ivar numUnloads:
    :ivar unloadAmount:
    :ivar numBalanceInquirys:
    :ivar numPayFacCredit:
    :ivar numPayFacDebit:
    :ivar numSubmerchantCredit:
    :ivar numSubmerchantDebit:
    :ivar numReserveCredit:
    :ivar numReserveDebit:
    :ivar numVendorDebit:
    :ivar numVendorCredit:
    :ivar numPhysicalCheckDebit:
    :ivar numPhysicalCheckCredit:
    :ivar numFundingInstructionVoid:
    :ivar numFastAccessFunding:
    :ivar numPayoutOrgCredit:
    :ivar numPayoutOrgDebit:
    :ivar numCustomerCredit:
    :ivar numCustomerDebit:
    :ivar numTranslateToLowValueTokenRequests:
    :ivar payFacCreditAmount:
    :ivar payFacDebitAmount:
    :ivar submerchantCreditAmount:
    :ivar submerchantDebitAmount:
    :ivar reserveCreditAmount:
    :ivar reserveDebitAmount:
    :ivar vendorDebitAmount:
    :ivar vendorCreditAmount:
    :ivar physicalCheckDebitAmount:
    :ivar physicalCheckCreditAmount:
    :ivar fastAccessFundingAmount:
    :ivar payoutOrgCreditAmount:
    :ivar payoutOrgDebitAmount:
    :ivar customerCreditAmount:
    :ivar customerDebitAmount:
    :ivar sameDayFunding:
    :ivar merchantId:
    """
    class Meta:
        name = "batchRequest"
        namespace = "http://www.vantivcnp.com/schema"

    serviceStatusRequest: List[ServiceStatusRequest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    queryTransaction: List[QueryTransaction] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    unloadReversal: List[UnloadReversal] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    loadReversal: List[LoadReversal] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    deactivateReversal: List[DeactivateReversal] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    activateReversal: List[ActivateReversal] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    refundReversal: List[RefundReversal] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    depositReversal: List[DepositReversal] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    echeckVoid: List[EcheckVoid] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    void: List[Void] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    customerDebit: List[CustomerDebit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    customerCredit: List[CustomerCredit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    submerchantDebit: List[SubmerchantDebit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    submerchantCredit: List[SubmerchantCredit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    vendorDebit: List[VendorDebit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    vendorCredit: List[VendorCredit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    echeckPreNoteCredit: List[EcheckPreNoteCredit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    echeckPreNoteSale: List[EcheckPreNoteSale] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    accountUpdate: List[AccountUpdate] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    transactionReversal: List[TransactionReversal] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    translateToLowValueTokenRequest: List[TranslateToLowValueTokenRequest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    payoutOrgCredit: List[PayoutOrgCredit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    payoutOrgDebit: List[PayoutOrgDebit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    fastAccessFunding: List[FastAccessFunding] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    fundingInstructionVoid: List[FundingInstructionVoid] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    physicalCheckDebit: List[PhysicalCheckDebit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    physicalCheckCredit: List[PhysicalCheckCredit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    reserveDebit: List[ReserveDebit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    reserveCredit: List[ReserveCredit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    payFacCredit: List[PayFacCredit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    payFacDebit: List[PayFacDebit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    fraudCheck: List[FraudCheck] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    echeckRedeposit: List[EcheckRedeposit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    echeckVerification: List[EcheckVerification] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    echeckCredit: List[EcheckCredit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    echeckSale: List[EcheckSale] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    registerTokenRequest: List[RegisterTokenRequest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    balanceInquiry: List[BalanceInquiry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    unload: List[Unload] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    load: List[Load] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    deactivate: List[Deactivate] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    activate: List[Activate] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    giftCardCredit: List[GiftCardCredit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    credit: List[Credit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    sale: List[Sale] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    captureGivenAuth: List[CaptureGivenAuth] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    forceCapture: List[ForceCapture] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    giftCardCapture: List[GiftCardCapture] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    capture: List[Capture] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    giftCardAuthReversal: List[GiftCardAuthReversal] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    authReversal: List[AuthReversal] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    authorization: List[Authorization] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    updateCardValidationNumOnToken: List[UpdateCardValidationNumOnToken] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    transaction: List[Transaction] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    updatePlan: List[UpdatePlan] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    createPlan: List[CreatePlan] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    updateSubscription: List[UpdateSubscription] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    cancelSubscription: List[CancelSubscription] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    recurringTransaction: List[RecurringTransaction] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    merchantSdk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    numAuths: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    authAmount: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numAuthReversals: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    authReversalAmount: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numTransactionReversals: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    transactionReversalAmount: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numGiftCardAuthReversals: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    giftCardAuthReversalOriginalAmount: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numCaptures: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    captureAmount: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numGiftCardCaptures: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    giftCardCaptureAmount: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numExtCaptures: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    extCaptureAmount: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numCredits: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    creditAmount: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numGiftCardCredits: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    giftCardCreditAmount: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numForceCaptures: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    forceCaptureAmount: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numSales: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    saleAmount: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numCaptureGivenAuths: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    captureGivenAuthAmount: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numEcheckSales: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    echeckSalesAmount: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numEcheckCredit: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    echeckCreditAmount: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numEcheckVerification: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    echeckVerificationAmount: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numEcheckRedeposit: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numEcheckPreNoteSale: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numEcheckPreNoteCredit: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numAccountUpdates: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numTokenRegistrations: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numUpdateCardValidationNumOnTokens: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numCancelSubscriptions: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numUpdateSubscriptions: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numCreatePlans: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numUpdatePlans: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numActivates: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numDeactivates: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    activateAmount: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numLoads: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    loadAmount: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numUnloads: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    unloadAmount: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numBalanceInquirys: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numPayFacCredit: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numPayFacDebit: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numSubmerchantCredit: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numSubmerchantDebit: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numReserveCredit: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numReserveDebit: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numVendorDebit: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numVendorCredit: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numPhysicalCheckDebit: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numPhysicalCheckCredit: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numFundingInstructionVoid: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numFastAccessFunding: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numPayoutOrgCredit: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numPayoutOrgDebit: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numCustomerCredit: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numCustomerDebit: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    numTranslateToLowValueTokenRequests: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    payFacCreditAmount: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    payFacDebitAmount: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    submerchantCreditAmount: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    submerchantDebitAmount: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    reserveCreditAmount: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    reserveDebitAmount: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    vendorDebitAmount: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    vendorCreditAmount: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    physicalCheckDebitAmount: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    physicalCheckCreditAmount: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    fastAccessFundingAmount: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    payoutOrgCreditAmount: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    payoutOrgDebitAmount: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    customerCreditAmount: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    customerDebitAmount: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    sameDayFunding: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    merchantId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class QueryTransactionResponse(TransactionTypeWithReportGroup):
    """
    :ivar response:
    :ivar responseTime:
    :ivar message:
    :ivar location:
    :ivar matchCount:
    :ivar resultsMax10:
    """
    class Meta:
        name = "queryTransactionResponse"
        namespace = "http://www.vantivcnp.com/schema"

    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    responseTime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    matchCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    resultsMax10: Optional["QueryTransactionResponse.ResultsMax10"] = field(
        default=None,
        metadata={
            "name": "results_max10",
            "type": "Element",
        }
    )

    @dataclass
    class ResultsMax10:
        """
        :ivar serviceStatusResponse:
        :ivar queryTransactionUnavailableResponse:
        :ivar queryTransactionResponse:
        :ivar echeckVoidResponse:
        :ivar voidResponse:
        :ivar echeckPreNoteCreditResponse:
        :ivar echeckPreNoteSaleResponse:
        :ivar accountUpdateResponse:
        :ivar transactionReversalResponse:
        :ivar translateToLowValueTokenResponse:
        :ivar payoutOrgDebitResponse:
        :ivar payoutOrgCreditResponse:
        :ivar customerDebitResponse:
        :ivar customerCreditResponse:
        :ivar fastAccessFundingResponse:
        :ivar fundingInstructionVoidResponse:
        :ivar vendorCreditResponse:
        :ivar vendorDebitResponse:
        :ivar physicalCheckDebitResponse:
        :ivar physicalCheckCreditResponse:
        :ivar reserveDebitResponse:
        :ivar reserveCreditResponse:
        :ivar payFacDebitResponse:
        :ivar payFacCreditResponse:
        :ivar submerchantDebitResponse:
        :ivar submerchantCreditResponse:
        :ivar fraudCheckResponse:
        :ivar updateCardValidationNumOnTokenResponse:
        :ivar echeckRedepositResponse:
        :ivar echeckVerificationResponse:
        :ivar echeckCreditResponse:
        :ivar echeckSalesResponse:
        :ivar deactivateResponse:
        :ivar balanceInquiryResponse:
        :ivar unloadResponse:
        :ivar loadResponse:
        :ivar activateResponse:
        :ivar giftCardCreditResponse:
        :ivar creditResponse:
        :ivar saleResponse:
        :ivar captureGivenAuthResponse:
        :ivar forceCaptureResponse:
        :ivar giftCardCaptureResponse:
        :ivar captureResponse:
        :ivar unloadReversalResponse:
        :ivar loadReversalResponse:
        :ivar deactivateReversalResponse:
        :ivar activateReversalResponse:
        :ivar refundReversalResponse:
        :ivar depositReversalResponse:
        :ivar giftCardAuthReversalResponse:
        :ivar authReversalResponse:
        :ivar authorizationResponse:
        :ivar registerTokenResponse:
        :ivar transactionResponse:
        """
        serviceStatusResponse: List[ServiceStatusResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        queryTransactionUnavailableResponse: List[QueryTransactionUnavailableResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        queryTransactionResponse: List["QueryTransactionResponse"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        echeckVoidResponse: List[EcheckVoidResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        voidResponse: List[VoidResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        echeckPreNoteCreditResponse: List[EcheckPreNoteCreditResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        echeckPreNoteSaleResponse: List[EcheckPreNoteSaleResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        accountUpdateResponse: List[AccountUpdateResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        transactionReversalResponse: List[TransactionReversalResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        translateToLowValueTokenResponse: List[TranslateToLowValueTokenResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        payoutOrgDebitResponse: List[PayoutOrgDebitResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        payoutOrgCreditResponse: List[PayoutOrgCreditResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        customerDebitResponse: List[CustomerDebitResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        customerCreditResponse: List[CustomerCreditResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        fastAccessFundingResponse: List[FastAccessFundingResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        fundingInstructionVoidResponse: List[FundingInstructionVoidResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        vendorCreditResponse: List[VendorCreditResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        vendorDebitResponse: List[VendorDebitResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        physicalCheckDebitResponse: List[PhysicalCheckDebitResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        physicalCheckCreditResponse: List[PhysicalCheckCreditResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        reserveDebitResponse: List[ReserveDebitResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        reserveCreditResponse: List[ReserveCreditResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        payFacDebitResponse: List[PayFacDebitResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        payFacCreditResponse: List[PayFacCreditResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        submerchantDebitResponse: List[SubmerchantDebitResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        submerchantCreditResponse: List[SubmerchantCreditResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        fraudCheckResponse: List[FraudCheckResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        updateCardValidationNumOnTokenResponse: List[UpdateCardValidationNumOnTokenResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        echeckRedepositResponse: List[EcheckRedepositResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        echeckVerificationResponse: List[EcheckVerificationResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        echeckCreditResponse: List[EcheckCreditResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        echeckSalesResponse: List[EcheckSalesResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        deactivateResponse: List[DeactivateResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        balanceInquiryResponse: List[BalanceInquiryResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        unloadResponse: List[UnloadResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        loadResponse: List[LoadResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        activateResponse: List[ActivateResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        giftCardCreditResponse: List[GiftCardCreditResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        creditResponse: List[CreditResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        saleResponse: List[SaleResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        captureGivenAuthResponse: List[CaptureGivenAuthResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        forceCaptureResponse: List[ForceCaptureResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        giftCardCaptureResponse: List[GiftCardCaptureResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        captureResponse: List[CaptureResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        unloadReversalResponse: List[UnloadReversalResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        loadReversalResponse: List[LoadReversalResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        deactivateReversalResponse: List[DeactivateReversalResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        activateReversalResponse: List[ActivateReversalResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        refundReversalResponse: List[RefundReversalResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        depositReversalResponse: List[DepositReversalResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        giftCardAuthReversalResponse: List[GiftCardAuthReversalResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        authReversalResponse: List[AuthReversalResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        authorizationResponse: List[AuthorizationResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        registerTokenResponse: List[RegisterTokenResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )
        transactionResponse: List[TransactionResponse] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 10,
            }
        )


@dataclass
class BatchResponse:
    """
    :ivar serviceStatusResponse:
    :ivar queryTransactionUnavailableResponse:
    :ivar queryTransactionResponse:
    :ivar echeckVoidResponse:
    :ivar voidResponse:
    :ivar echeckPreNoteCreditResponse:
    :ivar echeckPreNoteSaleResponse:
    :ivar accountUpdateResponse:
    :ivar transactionReversalResponse:
    :ivar translateToLowValueTokenResponse:
    :ivar payoutOrgDebitResponse:
    :ivar payoutOrgCreditResponse:
    :ivar customerDebitResponse:
    :ivar customerCreditResponse:
    :ivar fastAccessFundingResponse:
    :ivar fundingInstructionVoidResponse:
    :ivar vendorCreditResponse:
    :ivar vendorDebitResponse:
    :ivar physicalCheckDebitResponse:
    :ivar physicalCheckCreditResponse:
    :ivar reserveDebitResponse:
    :ivar reserveCreditResponse:
    :ivar payFacDebitResponse:
    :ivar payFacCreditResponse:
    :ivar submerchantDebitResponse:
    :ivar submerchantCreditResponse:
    :ivar fraudCheckResponse:
    :ivar updateCardValidationNumOnTokenResponse:
    :ivar echeckRedepositResponse:
    :ivar echeckVerificationResponse:
    :ivar echeckCreditResponse:
    :ivar echeckSalesResponse:
    :ivar deactivateResponse:
    :ivar balanceInquiryResponse:
    :ivar unloadResponse:
    :ivar loadResponse:
    :ivar activateResponse:
    :ivar giftCardCreditResponse:
    :ivar creditResponse:
    :ivar saleResponse:
    :ivar captureGivenAuthResponse:
    :ivar forceCaptureResponse:
    :ivar giftCardCaptureResponse:
    :ivar captureResponse:
    :ivar unloadReversalResponse:
    :ivar loadReversalResponse:
    :ivar deactivateReversalResponse:
    :ivar activateReversalResponse:
    :ivar refundReversalResponse:
    :ivar depositReversalResponse:
    :ivar giftCardAuthReversalResponse:
    :ivar authReversalResponse:
    :ivar authorizationResponse:
    :ivar registerTokenResponse:
    :ivar transactionResponse:
    :ivar updatePlanResponse:
    :ivar createPlanResponse:
    :ivar updateSubscriptionResponse:
    :ivar cancelSubscriptionResponse:
    :ivar recurringTransactionResponse:
    :ivar id:
    :ivar cnpBatchId:
    :ivar merchantId:
    :ivar numAccountUpdates:
    """
    class Meta:
        name = "batchResponse"
        namespace = "http://www.vantivcnp.com/schema"

    serviceStatusResponse: List[ServiceStatusResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    queryTransactionUnavailableResponse: List[QueryTransactionUnavailableResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    queryTransactionResponse: List[QueryTransactionResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    echeckVoidResponse: List[EcheckVoidResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    voidResponse: List[VoidResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    echeckPreNoteCreditResponse: List[EcheckPreNoteCreditResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    echeckPreNoteSaleResponse: List[EcheckPreNoteSaleResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    accountUpdateResponse: List[AccountUpdateResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    transactionReversalResponse: List[TransactionReversalResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    translateToLowValueTokenResponse: List[TranslateToLowValueTokenResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    payoutOrgDebitResponse: List[PayoutOrgDebitResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    payoutOrgCreditResponse: List[PayoutOrgCreditResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    customerDebitResponse: List[CustomerDebitResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    customerCreditResponse: List[CustomerCreditResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    fastAccessFundingResponse: List[FastAccessFundingResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    fundingInstructionVoidResponse: List[FundingInstructionVoidResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    vendorCreditResponse: List[VendorCreditResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    vendorDebitResponse: List[VendorDebitResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    physicalCheckDebitResponse: List[PhysicalCheckDebitResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    physicalCheckCreditResponse: List[PhysicalCheckCreditResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    reserveDebitResponse: List[ReserveDebitResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    reserveCreditResponse: List[ReserveCreditResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    payFacDebitResponse: List[PayFacDebitResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    payFacCreditResponse: List[PayFacCreditResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    submerchantDebitResponse: List[SubmerchantDebitResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    submerchantCreditResponse: List[SubmerchantCreditResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    fraudCheckResponse: List[FraudCheckResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    updateCardValidationNumOnTokenResponse: List[UpdateCardValidationNumOnTokenResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    echeckRedepositResponse: List[EcheckRedepositResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    echeckVerificationResponse: List[EcheckVerificationResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    echeckCreditResponse: List[EcheckCreditResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    echeckSalesResponse: List[EcheckSalesResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    deactivateResponse: List[DeactivateResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    balanceInquiryResponse: List[BalanceInquiryResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    unloadResponse: List[UnloadResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    loadResponse: List[LoadResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    activateResponse: List[ActivateResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    giftCardCreditResponse: List[GiftCardCreditResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    creditResponse: List[CreditResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    saleResponse: List[SaleResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    captureGivenAuthResponse: List[CaptureGivenAuthResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    forceCaptureResponse: List[ForceCaptureResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    giftCardCaptureResponse: List[GiftCardCaptureResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    captureResponse: List[CaptureResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    unloadReversalResponse: List[UnloadReversalResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    loadReversalResponse: List[LoadReversalResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    deactivateReversalResponse: List[DeactivateReversalResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    activateReversalResponse: List[ActivateReversalResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    refundReversalResponse: List[RefundReversalResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    depositReversalResponse: List[DepositReversalResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    giftCardAuthReversalResponse: List[GiftCardAuthReversalResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    authReversalResponse: List[AuthReversalResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    authorizationResponse: List[AuthorizationResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    registerTokenResponse: List[RegisterTokenResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    transactionResponse: List[TransactionResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    updatePlanResponse: List[UpdatePlanResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    createPlanResponse: List[CreatePlanResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    updateSubscriptionResponse: List[UpdateSubscriptionResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    cancelSubscriptionResponse: List[CancelSubscriptionResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    recurringTransactionResponse: List[RecurringTransactionResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    cnpBatchId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    merchantId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    numAccountUpdates: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class CnpOnlineRequest(BaseRequest):
    """
    :ivar merchantId:
    :ivar merchantSdk:
    :ivar loggedInUser:
    :ivar sameDayFunding:
    """
    class Meta:
        name = "cnpOnlineRequest"
        namespace = "http://www.vantivcnp.com/schema"

    merchantId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    merchantSdk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    loggedInUser: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    sameDayFunding: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class CnpOnlineResponse:
    """
    :ivar serviceStatusResponse:
    :ivar queryTransactionUnavailableResponse:
    :ivar queryTransactionResponse:
    :ivar echeckVoidResponse:
    :ivar voidResponse:
    :ivar echeckPreNoteCreditResponse:
    :ivar echeckPreNoteSaleResponse:
    :ivar accountUpdateResponse:
    :ivar transactionReversalResponse:
    :ivar translateToLowValueTokenResponse:
    :ivar payoutOrgDebitResponse:
    :ivar payoutOrgCreditResponse:
    :ivar customerDebitResponse:
    :ivar customerCreditResponse:
    :ivar fastAccessFundingResponse:
    :ivar fundingInstructionVoidResponse:
    :ivar vendorCreditResponse:
    :ivar vendorDebitResponse:
    :ivar physicalCheckDebitResponse:
    :ivar physicalCheckCreditResponse:
    :ivar reserveDebitResponse:
    :ivar reserveCreditResponse:
    :ivar payFacDebitResponse:
    :ivar payFacCreditResponse:
    :ivar submerchantDebitResponse:
    :ivar submerchantCreditResponse:
    :ivar fraudCheckResponse:
    :ivar updateCardValidationNumOnTokenResponse:
    :ivar echeckRedepositResponse:
    :ivar echeckVerificationResponse:
    :ivar echeckCreditResponse:
    :ivar echeckSalesResponse:
    :ivar deactivateResponse:
    :ivar balanceInquiryResponse:
    :ivar unloadResponse:
    :ivar loadResponse:
    :ivar activateResponse:
    :ivar giftCardCreditResponse:
    :ivar creditResponse:
    :ivar saleResponse:
    :ivar captureGivenAuthResponse:
    :ivar forceCaptureResponse:
    :ivar giftCardCaptureResponse:
    :ivar captureResponse:
    :ivar unloadReversalResponse:
    :ivar loadReversalResponse:
    :ivar deactivateReversalResponse:
    :ivar activateReversalResponse:
    :ivar refundReversalResponse:
    :ivar depositReversalResponse:
    :ivar giftCardAuthReversalResponse:
    :ivar authReversalResponse:
    :ivar authorizationResponse:
    :ivar registerTokenResponse:
    :ivar transactionResponse:
    :ivar updatePlanResponse:
    :ivar createPlanResponse:
    :ivar updateSubscriptionResponse:
    :ivar cancelSubscriptionResponse:
    :ivar recurringTransactionResponse:
    :ivar response:
    :ivar message:
    :ivar version:
    """
    class Meta:
        name = "cnpOnlineResponse"
        namespace = "http://www.vantivcnp.com/schema"

    serviceStatusResponse: Optional[ServiceStatusResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    queryTransactionUnavailableResponse: Optional[QueryTransactionUnavailableResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    queryTransactionResponse: Optional[QueryTransactionResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    echeckVoidResponse: Optional[EcheckVoidResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    voidResponse: Optional[VoidResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    echeckPreNoteCreditResponse: Optional[EcheckPreNoteCreditResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    echeckPreNoteSaleResponse: Optional[EcheckPreNoteSaleResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    accountUpdateResponse: Optional[AccountUpdateResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    transactionReversalResponse: Optional[TransactionReversalResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    translateToLowValueTokenResponse: Optional[TranslateToLowValueTokenResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    payoutOrgDebitResponse: Optional[PayoutOrgDebitResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    payoutOrgCreditResponse: Optional[PayoutOrgCreditResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    customerDebitResponse: Optional[CustomerDebitResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    customerCreditResponse: Optional[CustomerCreditResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fastAccessFundingResponse: Optional[FastAccessFundingResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fundingInstructionVoidResponse: Optional[FundingInstructionVoidResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    vendorCreditResponse: Optional[VendorCreditResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    vendorDebitResponse: Optional[VendorDebitResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    physicalCheckDebitResponse: Optional[PhysicalCheckDebitResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    physicalCheckCreditResponse: Optional[PhysicalCheckCreditResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    reserveDebitResponse: Optional[ReserveDebitResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    reserveCreditResponse: Optional[ReserveCreditResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    payFacDebitResponse: Optional[PayFacDebitResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    payFacCreditResponse: Optional[PayFacCreditResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    submerchantDebitResponse: Optional[SubmerchantDebitResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    submerchantCreditResponse: Optional[SubmerchantCreditResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fraudCheckResponse: Optional[FraudCheckResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    updateCardValidationNumOnTokenResponse: Optional[UpdateCardValidationNumOnTokenResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    echeckRedepositResponse: Optional[EcheckRedepositResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    echeckVerificationResponse: Optional[EcheckVerificationResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    echeckCreditResponse: Optional[EcheckCreditResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    echeckSalesResponse: Optional[EcheckSalesResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    deactivateResponse: Optional[DeactivateResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    balanceInquiryResponse: Optional[BalanceInquiryResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    unloadResponse: Optional[UnloadResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    loadResponse: Optional[LoadResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    activateResponse: Optional[ActivateResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    giftCardCreditResponse: Optional[GiftCardCreditResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    creditResponse: Optional[CreditResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    saleResponse: Optional[SaleResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    captureGivenAuthResponse: Optional[CaptureGivenAuthResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    forceCaptureResponse: Optional[ForceCaptureResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    giftCardCaptureResponse: Optional[GiftCardCaptureResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    captureResponse: Optional[CaptureResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    unloadReversalResponse: Optional[UnloadReversalResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    loadReversalResponse: Optional[LoadReversalResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    deactivateReversalResponse: Optional[DeactivateReversalResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    activateReversalResponse: Optional[ActivateReversalResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    refundReversalResponse: Optional[RefundReversalResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    depositReversalResponse: Optional[DepositReversalResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    giftCardAuthReversalResponse: Optional[GiftCardAuthReversalResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    authReversalResponse: Optional[AuthReversalResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    authorizationResponse: Optional[AuthorizationResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    registerTokenResponse: Optional[RegisterTokenResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    transactionResponse: Optional[TransactionResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    updatePlanResponse: Optional[UpdatePlanResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    createPlanResponse: Optional[CreatePlanResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    updateSubscriptionResponse: Optional[UpdateSubscriptionResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    cancelSubscriptionResponse: Optional[CancelSubscriptionResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    recurringTransactionResponse: Optional[RecurringTransactionResponse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CnpRequest:
    """
    :ivar authentication:
    :ivar batchRequest:
    :ivar rfrrequest:
    :ivar version:
    :ivar id:
    :ivar numBatchRequests:
    """
    class Meta:
        name = "cnpRequest"
        namespace = "http://www.vantivcnp.com/schema"

    authentication: Optional[Authentication] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    batchRequest: List[BatchRequest] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    rfrrequest: Optional[RFRRequest] = field(
        default=None,
        metadata={
            "name": "RFRRequest",
            "type": "Element",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    numBatchRequests: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CnpResponse:
    """
    :ivar batchResponse:
    :ivar rfrresponse:
    :ivar version:
    :ivar id:
    :ivar response:
    :ivar message:
    :ivar cnpSessionId:
    """
    class Meta:
        name = "cnpResponse"
        namespace = "http://www.vantivcnp.com/schema"

    batchResponse: List[BatchResponse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    rfrresponse: Optional[RFRResponse] = field(
        default=None,
        metadata={
            "name": "RFRResponse",
            "type": "Element",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    cnpSessionId: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

from typing import List, Literal
import genicam as geni
import numpy as np

class DeviceInfo:
    def GetSerialNumber(self) -> str: ...
    def SetSerialNumber(self, SerialNumberValue: str) -> DeviceInfo: ...
    def IsSerialNumberAvailable(self) -> bool: ...
    def GetUserDefinedName(self) -> str: ...
    def SetUserDefinedName(self, UserDefinedNameValue: str) -> DeviceInfo: ...
    def IsUserDefinedNameAvailable(self) -> bool: ...
    def GetModelName(self) -> str: ...
    def SetModelName(self, ModelNameValue: str) -> DeviceInfo: ...
    def IsModelNameAvailable(self) -> bool: ...
    def GetDeviceVersion(self) -> str: ...
    def SetDeviceVersion(self, DeviceVersionValue: str) -> DeviceInfo: ...
    def IsDeviceVersionAvailable(self) -> bool: ...
    def GetDeviceFactory(self) -> str: ...
    def SetDeviceFactory(self, DeviceFactoryValue: str) -> DeviceInfo: ...
    def IsDeviceFactoryAvailable(self) -> bool: ...
    def GetXMLSource(self) -> str: ...
    def SetXMLSource(self, XMLSource: str) -> DeviceInfo: ...
    def IsXMLSourceAvailable(self) -> bool: ...
    def SetFriendlyName(self, FriendlyNameValue: str) -> DeviceInfo: ...
    def SetFullName(self, FullNameValue: str) -> DeviceInfo: ...
    def SetVendorName(self, VendorNameValue: str) -> DeviceInfo: ...
    def SetDeviceClass(self, DeviceClassValue: str) -> DeviceInfo: ...
    def GetDeviceClass(self) -> str: ...
    def GetInterfaceID(self) -> str: ...
    def SetInterfaceID(self, InterfaceIDValue: str) -> DeviceInfo: ...
    def IsInterfaceIDAvailable(self) -> bool: ...
    def GetAddress(self) -> str: ...
    def SetAddress(self, AddressValue: str) -> DeviceInfo: ...
    def IsAddressAvailable(self) -> bool: ...
    def GetIpAddress(self) -> str: ...
    def SetIpAddress(self, IpAddressValue: str) -> DeviceInfo: ...
    def IsIpAddressAvailable(self) -> bool: ...
    def GetSubnetAddress(self) -> str: ...
    def SetSubnetAddress(self, SubnetAddressValue: str) -> DeviceInfo: ...
    def IsSubnetAddressAvailable(self) -> bool: ...
    def GetDefaultGateway(self) -> str: ...
    def SetDefaultGateway(self, DefaultGatewayValue: str) -> DeviceInfo: ...
    def IsDefaultGatewayAvailable(self) -> bool: ...
    def GetSubnetMask(self) -> str: ...
    def SetSubnetMask(self, SubnetMaskValue: str) -> DeviceInfo: ...
    def IsSubnetMaskAvailable(self) -> bool: ...
    def GetPortNr(self) -> str: ...
    def SetPortNr(self, PortNrValue: str) -> DeviceInfo: ...
    def IsPortNrAvailable(self) -> bool: ...
    def GetMacAddress(self) -> str: ...
    def SetMacAddress(self, MacAddressValue: str) -> DeviceInfo: ...
    def IsMacAddressAvailable(self) -> bool: ...
    def GetInterface(self) -> str: ...
    def SetInterface(self, InterfaceValue: str) -> DeviceInfo: ...
    def IsInterfaceAvailable(self) -> bool: ...
    def GetIpConfigOptions(self) -> str: ...
    def SetIpConfigOptions(self, IpConfigOptionsValue: str) -> DeviceInfo: ...
    def IsIpConfigOptionsAvailable(self) -> bool: ...
    def GetIpConfigCurrent(self) -> str: ...
    def SetIpConfigCurrent(self, IpConfigCurrentValue: str) -> DeviceInfo: ...
    def IsIpConfigCurrentAvailable(self) -> bool: ...
    def GetDeviceGUID(self) -> str: ...
    def IsDeviceGUIDAvailable(self) -> bool: ...
    def GetManufacturerInfo(self) -> str: ...
    def IsManufacturerInfoAvailable(self) -> bool: ...
    def GetDeviceIdx(self) -> str: ...
    def IsDeviceIdxAvailable(self) -> bool: ...
    def GetProductId(self) -> str: ...
    def IsProductIdAvailable(self) -> bool: ...
    def GetVendorId(self) -> str: ...
    def IsVendorIdAvailable(self) -> bool: ...
    def GetDriverKeyName(self) -> str: ...
    def IsDriverKeyNameAvailable(self) -> bool: ...
    def GetUsbDriverType(self) -> str: ...
    def IsUsbDriverTypeAvailable(self) -> bool: ...
    def GetTransferMode(self) -> str: ...
    def IsTransferModeAvailable(self) -> bool: ...
    def GetInternalName(self) -> str: ...
    def SetInternalName(self, InternalNameValue: str) -> DeviceInfo: ...
    def IsInternalNameAvailable(self) -> bool: ...
    def GetBconAdapterLibraryName(self) -> str: ...
    def SetBconAdapterLibraryName(
        self, BconAdapterLibraryNameValue: str
    ) -> DeviceInfo: ...
    def IsBconAdapterLibraryNameAvailable(self) -> bool: ...
    def GetBconAdapterLibraryVersion(self) -> str: ...
    def SetBconAdapterLibraryVersion(
        self, BconAdapterLibraryVersionValue: str
    ) -> DeviceInfo: ...
    def IsBconAdapterLibraryVersionAvailable(self) -> bool: ...
    def GetBconAdapterLibraryApiVersion(self) -> str: ...
    def SetBconAdapterLibraryApiVersion(
        self, BconAdapterLibraryApiVersionValue: str
    ) -> DeviceInfo: ...
    def IsBconAdapterLibraryApiVersionAvailable(self) -> bool: ...
    def GetSupportedBconAdapterApiVersion(self) -> str: ...
    def SetSupportedBconAdapterApiVersion(
        self, SupportedBconAdapterApiVersionValue: str
    ) -> DeviceInfo: ...
    def IsSupportedBconAdapterApiVersionAvailable(self) -> bool: ...
    def GetPortID(self) -> str: ...
    def SetPortID(self, PortIDValue: str) -> DeviceInfo: ...
    def IsPortIDAvailable(self) -> bool: ...
    def GetDeviceID(self) -> str: ...
    def SetDeviceID(self, DeviceIDValue: str) -> DeviceInfo: ...
    def IsDeviceIDAvailable(self) -> bool: ...
    def GetInitialBaudRate(self) -> str: ...
    def SetInitialBaudRate(self, InitialBaudRateValue: str) -> DeviceInfo: ...
    def IsInitialBaudRateAvailable(self) -> bool: ...
    def GetDeviceXMLFileOverride(self) -> str: ...
    def SetDeviceXMLFileOverride(
        self, DeviceXMLFileOverrideValue: str
    ) -> DeviceInfo: ...
    def IsDeviceXMLFileOverrideAvailable(self) -> bool: ...
    def GetDeviceSpecificString(self) -> str: ...
    def SetDeviceSpecificString(self, DeviceSpecificStringValue: str) -> DeviceInfo: ...
    def IsDeviceSpecificStringAvailable(self) -> bool: ...
    def GetPortSpecificString(self) -> str: ...
    def SetPortSpecificString(self, PortSpecificStringValue: str) -> DeviceInfo: ...
    def IsPortSpecificStringAvailable(self) -> bool: ...
    def SetPropertyValue(self, Name: str, Value: str) -> DeviceInfo: ...
    def IsPersistentIpActive(self) -> bool: ...
    def IsDhcpActive(self) -> bool: ...
    def IsAutoIpActive(self) -> bool: ...
    def IsPersistentIpSupported(self) -> bool: ...
    def IsDhcpSupported(self) -> bool: ...
    def IsAutoIpSupported(self) -> bool: ...

class IPylonDevice:
    pass

class TlFactory:
    @staticmethod
    def GetInstance() -> TlFactory: ...

    # def CreateTl(self, tl_name:str ) -> ITransportLayer: ...

    def EnumerateDevices(self, di: List[DeviceInfo] = ...) -> List[DeviceInfo]: ...
    def CreateFirstDevice(self, di: DeviceInfo = ...) -> IPylonDevice: ...
    def CreateDevice(self, di: DeviceInfo) -> IPylonDevice: ...

class UniversalCameraFeatures:
    AcquisitionAbort: geni.ICommand
    AcquisitionBurstFrameCount: geni.IInteger
    AcquisitionFrameCount: geni.IInteger
    AcquisitionFrameRate: geni.IFloat
    AcquisitionFrameRateAbs: geni.IFloat
    AcquisitionFrameRateEnable: geni.IBoolean
    AcquisitionFrameRateEnum: geni.IEnumeration
    AcquisitionIdle: geni.IBoolean
    AcquisitionLineRateAbs: geni.IFloat
    AcquisitionMode: geni.IEnumeration
    AcquisitionStart: geni.ICommand
    AcquisitionStartEventStreamChannelIndex: geni.IInteger
    AcquisitionStartEventTimestamp: geni.IInteger
    AcquisitionStartOvertriggerEventStreamChannelIndex: geni.IInteger
    AcquisitionStartOvertriggerEventTimestamp: geni.IInteger
    AcquisitionStartWaitEventStreamChannelIndex: geni.IInteger
    AcquisitionStartWaitEventTimestamp: geni.IInteger
    AcquisitionStatus: geni.IBoolean
    AcquisitionStatusSelector: geni.IEnumeration
    AcquisitionStop: geni.ICommand
    AcquisitionWaitEventStreamChannelIndex: geni.IInteger
    AcquisitionWaitEventTimestamp: geni.IInteger
    ActionCommandCount: geni.IInteger
    ActionDeviceKey: geni.IInteger
    ActionGroupKey: geni.IInteger
    ActionGroupMask: geni.IInteger
    ActionLateEventStreamChannelIndex: geni.IInteger
    ActionLateEventTimestamp: geni.IInteger
    ActionQueueSize: geni.IInteger
    ActionSelector: geni.IInteger
    AutoBacklightCompensation: geni.IFloat
    AutoExposureTimeAbsLowerLimit: geni.IFloat
    AutoExposureTimeAbsUpperLimit: geni.IFloat
    AutoExposureTimeLowerLimit: geni.IFloat
    AutoExposureTimeLowerLimitRaw: geni.IInteger
    AutoExposureTimeUpperLimit: geni.IFloat
    AutoExposureTimeUpperLimitRaw: geni.IInteger
    AutoFunctionAOIHeight: geni.IInteger
    AutoFunctionAOIOffsetX: geni.IInteger
    AutoFunctionAOIOffsetY: geni.IInteger
    AutoFunctionAOISelector: geni.IEnumeration
    AutoFunctionAOIUsageIntensity: geni.IBoolean
    AutoFunctionAOIUsageRedLightCorrection: geni.IBoolean
    AutoFunctionAOIUsageTonalRange: geni.IBoolean
    AutoFunctionAOIUsageWhiteBalance: geni.IBoolean
    AutoFunctionAOIUseBrightness: geni.IBoolean
    AutoFunctionAOIUseWhiteBalance: geni.IBoolean
    AutoFunctionAOIWidth: geni.IInteger
    AutoFunctionProfile: geni.IEnumeration
    AutoFunctionROIHeight: geni.IInteger
    AutoFunctionROIHighlight: geni.IBoolean
    AutoFunctionROIOffsetX: geni.IInteger
    AutoFunctionROIOffsetY: geni.IInteger
    AutoFunctionROISelector: geni.IEnumeration
    AutoFunctionROIUseBrightness: geni.IBoolean
    AutoFunctionROIUseTonalRange: geni.IBoolean
    AutoFunctionROIUseWhiteBalance: geni.IBoolean
    AutoFunctionROIWidth: geni.IInteger
    AutoGainLowerLimit: geni.IFloat
    AutoGainRawLowerLimit: geni.IInteger
    AutoGainRawUpperLimit: geni.IInteger
    AutoGainUpperLimit: geni.IFloat
    AutoTargetBrightness: geni.IFloat
    AutoTargetBrightnessDamping: geni.IFloat
    AutoTargetValue: geni.IInteger
    AutoTonalRangeAdjustmentSelector: geni.IEnumeration
    AutoTonalRangeModeSelector: geni.IEnumeration
    AutoTonalRangeTargetBright: geni.IInteger
    AutoTonalRangeTargetDark: geni.IInteger
    AutoTonalRangeThresholdBright: geni.IFloat
    AutoTonalRangeThresholdBrightRaw: geni.IInteger
    AutoTonalRangeThresholdDark: geni.IFloat
    AutoTonalRangeThresholdDarkRaw: geni.IInteger
    BLCSerialFramingError: geni.IBoolean
    BLCSerialParityError: geni.IBoolean
    BLCSerialPortBaudRate: geni.IEnumeration
    BLCSerialPortClearErrors: geni.ICommand
    BLCSerialPortParity: geni.IEnumeration
    BLCSerialPortReceiveCmd: geni.ICommand
    BLCSerialPortReceiveValue: geni.IInteger
    BLCSerialPortSource: geni.IEnumeration
    BLCSerialPortStopBits: geni.IEnumeration
    BLCSerialPortTransmitCmd: geni.ICommand
    BLCSerialPortTransmitValue: geni.IInteger
    BLCSerialReceiveQueueStatus: geni.IEnumeration
    BLCSerialTransmitQueueStatus: geni.IEnumeration
    BalanceRatio: geni.IFloat
    BalanceRatioAbs: geni.IFloat
    BalanceRatioRaw: geni.IInteger
    BalanceRatioSelector: geni.IEnumeration
    BalanceWhiteAdjustmentDampingAbs: geni.IFloat
    BalanceWhiteAdjustmentDampingRaw: geni.IInteger
    BalanceWhiteAuto: geni.IEnumeration
    BalanceWhiteReset: geni.ICommand
    BandwidthReserveMode: geni.IEnumeration
    BinningHorizontal: geni.IInteger
    BinningHorizontalMode: geni.IEnumeration
    BinningModeHorizontal: geni.IEnumeration
    BinningModeVertical: geni.IEnumeration
    BinningSelector: geni.IEnumeration
    BinningVertical: geni.IInteger
    BinningVerticalMode: geni.IEnumeration
    BlackLevel: geni.IFloat
    BlackLevelAbs: geni.IFloat
    BlackLevelRaw: geni.IInteger
    BlackLevelSelector: geni.IEnumeration
    BslAcquisitionBurstMode: geni.IEnumeration
    BslAcquisitionStopMode: geni.IEnumeration
    BslAdaptiveToneMappingMode: geni.IEnumeration
    BslBlackLevelCompensationMode: geni.IEnumeration
    BslBrightness: geni.IFloat
    BslBrightnessRaw: geni.IInteger
    BslCenterX: geni.ICommand
    BslCenterY: geni.ICommand
    BslChunkAutoBrightnessStatus: geni.IEnumeration
    BslChunkTimestampSelector: geni.IEnumeration
    BslChunkTimestampValue: geni.IInteger
    BslColorAdjustmentEnable: geni.IBoolean
    BslColorAdjustmentHue: geni.IFloat
    BslColorAdjustmentSaturation: geni.IFloat
    BslColorAdjustmentSelector: geni.IEnumeration
    BslColorSpace: geni.IEnumeration
    BslColorSpaceMode: geni.IEnumeration
    BslContrast: geni.IFloat
    BslContrastMode: geni.IEnumeration
    BslContrastRaw: geni.IInteger
    BslDefectPixelCorrectionMode: geni.IEnumeration
    BslDeviceLinkCurrentThroughput: geni.IInteger
    BslEffectiveExposureTime: geni.IFloat
    BslErrorPresent: geni.IBoolean
    BslErrorReportNext: geni.ICommand
    BslErrorReportValue: geni.IInteger
    BslExposureStartDelay: geni.IFloat
    BslExposureTimeMode: geni.IEnumeration
    BslHue: geni.IFloat
    BslHueRaw: geni.IInteger
    BslHueValue: geni.IInteger
    BslImageCompressionLastRatio: geni.IFloat
    BslImageCompressionLastSize: geni.IInteger
    BslImageCompressionRatio: geni.IFloat
    BslImmediateTriggerMode: geni.IEnumeration
    BslInputFilterTime: geni.IFloat
    BslInputHoldOffTime: geni.IFloat
    BslLightControlEnumerateDevices: geni.ICommand
    BslLightControlErrorStatus: geni.IEnumeration
    BslLightControlMode: geni.IEnumeration
    BslLightControlSource: geni.IEnumeration
    BslLightControlStatus: geni.IEnumeration
    BslLightDeviceBrightness: geni.IFloat
    BslLightDeviceBrightnessRaw: geni.IInteger
    BslLightDeviceChangeID: geni.IEnumeration
    BslLightDeviceClearLastError: geni.ICommand
    BslLightDeviceFirmwareVersion: geni.IString
    BslLightDeviceLastError: geni.IEnumeration
    BslLightDeviceMaxCurrent: geni.IFloat
    BslLightDeviceMaxCurrentRaw: geni.IInteger
    BslLightDeviceOperationMode: geni.IEnumeration
    BslLightDeviceSelector: geni.IEnumeration
    BslLightDeviceStrobeDuration: geni.IFloat
    BslLightDeviceStrobeDurationRaw: geni.IInteger
    BslLightDeviceStrobeMode: geni.IEnumeration
    BslLightSourcePreset: geni.IEnumeration
    BslLightSourcePresetFeatureEnable: geni.IBoolean
    BslLightSourcePresetFeatureSelector: geni.IEnumeration
    BslLineConnection: geni.IEnumeration
    BslLineOverloadStatus: geni.IBoolean
    BslMultipleROIColumnOffset: geni.IInteger
    BslMultipleROIColumnSelector: geni.IEnumeration
    BslMultipleROIColumnSize: geni.IInteger
    BslMultipleROIColumnsEnable: geni.IBoolean
    BslMultipleROIRowOffset: geni.IInteger
    BslMultipleROIRowSelector: geni.IEnumeration
    BslMultipleROIRowSize: geni.IInteger
    BslMultipleROIRowsEnable: geni.IBoolean
    BslNoiseReduction: geni.IFloat
    BslPeriodicSignalActivation: geni.IEnumeration
    BslPeriodicSignalDelay: geni.IFloat
    BslPeriodicSignalPeriod: geni.IFloat
    BslPeriodicSignalSelector: geni.IEnumeration
    BslPeriodicSignalSource: geni.IEnumeration
    BslPtpDelayMechanism: geni.IEnumeration
    BslPtpManagementEnable: geni.IBoolean
    BslPtpNetworkMode: geni.IEnumeration
    BslPtpPriority1: geni.IInteger
    BslPtpProfile: geni.IEnumeration
    BslPtpTwoStep: geni.IBoolean
    BslPtpUcPortAddr: geni.IInteger
    BslPtpUcPortAddrIndex: geni.IInteger
    BslResultingAcquisitionFrameRate: geni.IFloat
    BslResultingFrameBurstRate: geni.IFloat
    BslResultingTransferFrameRate: geni.IFloat
    BslSaturation: geni.IFloat
    BslSaturationRaw: geni.IInteger
    BslSaturationValue: geni.IFloat
    BslScaledSensorHeight: geni.IInteger
    BslScaledSensorWidth: geni.IInteger
    BslScalingEnable: geni.IBoolean
    BslScalingFactor: geni.IFloat
    BslSensorBitDepth: geni.IEnumeration
    BslSensorBitDepthMode: geni.IEnumeration
    BslSensorOff: geni.ICommand
    BslSensorOn: geni.ICommand
    BslSensorStandby: geni.ICommand
    BslSensorState: geni.IEnumeration
    BslSerialBaudRate: geni.IEnumeration
    BslSerialNumberOfDataBits: geni.IEnumeration
    BslSerialNumberOfStopBits: geni.IEnumeration
    BslSerialParity: geni.IEnumeration
    BslSerialReceive: geni.ICommand
    BslSerialRxBreak: geni.IBoolean
    BslSerialRxBreakReset: geni.ICommand
    BslSerialRxFifoOverflow: geni.IBoolean
    BslSerialRxParityError: geni.IBoolean
    BslSerialRxSource: geni.IEnumeration
    BslSerialRxStopBitError: geni.IBoolean
    BslSerialTransferBuffer: geni.IRegister
    BslSerialTransferLength: geni.IInteger
    BslSerialTransmit: geni.ICommand
    BslSerialTxBreak: geni.IBoolean
    BslSerialTxFifoEmpty: geni.IBoolean
    BslSerialTxFifoOverflow: geni.IBoolean
    BslSharpnessEnhancement: geni.IFloat
    BslTemperatureMax: geni.IFloat
    BslTemperatureStatus: geni.IEnumeration
    BslTemperatureStatusErrorCount: geni.IInteger
    BslTransferBitDepth: geni.IEnumeration
    BslTransferBitDepthMode: geni.IEnumeration
    BslTwiBitrate: geni.IEnumeration
    BslTwiPullSclLow: geni.IBoolean
    BslTwiPullSdaLow: geni.IBoolean
    BslTwiRead: geni.ICommand
    BslTwiTargetAddress: geni.IInteger
    BslTwiTransferBuffer: geni.IRegister
    BslTwiTransferLength: geni.IInteger
    BslTwiTransferStatus: geni.IEnumeration
    BslTwiUpdateTransferStatus: geni.ICommand
    BslTwiWrite: geni.ICommand
    BslUSBPowerSource: geni.IEnumeration
    BslUSBSpeedMode: geni.IEnumeration
    BslV4lDevicePath: geni.IString
    BslVignettingCorrectionLoad: geni.ICommand
    BslVignettingCorrectionMode: geni.IEnumeration
    CameraOperationMode: geni.IEnumeration
    CenterX: geni.IBoolean
    CenterY: geni.IBoolean
    ChunkCounterSelector: geni.IEnumeration
    ChunkCounterValue: geni.IInteger
    ChunkDynamicRangeMax: geni.IInteger
    ChunkDynamicRangeMin: geni.IInteger
    ChunkEnable: geni.IBoolean
    ChunkExposureTime: geni.IFloat
    ChunkFrameID: geni.IInteger
    ChunkFrameTriggerCounter: geni.IInteger
    ChunkFrameTriggerIgnoredCounter: geni.IInteger
    ChunkFramecounter: geni.IInteger
    ChunkFramesPerTriggerCounter: geni.IInteger
    ChunkGain: geni.IFloat
    ChunkGainAll: geni.IInteger
    ChunkGainSelector: geni.IEnumeration
    ChunkHeight: geni.IInteger
    ChunkInputStatusAtLineTriggerBitsPerLine: geni.IInteger
    ChunkInputStatusAtLineTriggerIndex: geni.IInteger
    ChunkInputStatusAtLineTriggerValue: geni.IInteger
    ChunkLineStatusAll: geni.IInteger
    ChunkLineTriggerCounter: geni.IInteger
    ChunkLineTriggerEndToEndCounter: geni.IInteger
    ChunkLineTriggerIgnoredCounter: geni.IInteger
    ChunkModeActive: geni.IBoolean
    ChunkOffsetX: geni.IInteger
    ChunkOffsetY: geni.IInteger
    ChunkPayloadCRC16: geni.IInteger
    ChunkPixelFormat: geni.IEnumeration
    ChunkSelector: geni.IEnumeration
    ChunkSequenceSetIndex: geni.IInteger
    ChunkSequencerSetActive: geni.IInteger
    ChunkShaftEncoderCounter: geni.IInteger
    ChunkStride: geni.IInteger
    ChunkTimestamp: geni.IInteger
    ChunkTriggerinputcounter: geni.IInteger
    ChunkVirtLineStatusAll: geni.IInteger
    ChunkWidth: geni.IInteger
    ClConfiguration: geni.IEnumeration
    ClInterLineDelayAbs: geni.IFloat
    ClInterLineDelayRaw: geni.IInteger
    ClPixelClock: geni.IEnumeration
    ClPixelClockAbs: geni.IFloat
    ClSerialPortBaudRate: geni.IEnumeration
    ClTapGeometry: geni.IEnumeration
    ClTimeSlots: geni.IEnumeration
    ClearLastError: geni.ICommand
    ColorAdjustmentEnable: geni.IBoolean
    ColorAdjustmentHue: geni.IFloat
    ColorAdjustmentHueRaw: geni.IInteger
    ColorAdjustmentReset: geni.ICommand
    ColorAdjustmentSaturation: geni.IFloat
    ColorAdjustmentSaturationRaw: geni.IInteger
    ColorAdjustmentSelector: geni.IEnumeration
    ColorOverexposureCompensationAOIEnable: geni.IBoolean
    ColorOverexposureCompensationAOIFactor: geni.IFloat
    ColorOverexposureCompensationAOIFactorRaw: geni.IInteger
    ColorOverexposureCompensationAOIHeight: geni.IInteger
    ColorOverexposureCompensationAOIOffsetX: geni.IInteger
    ColorOverexposureCompensationAOIOffsetY: geni.IInteger
    ColorOverexposureCompensationAOISelector: geni.IEnumeration
    ColorOverexposureCompensationAOIWidth: geni.IInteger
    ColorSpace: geni.IEnumeration
    ColorTransformationEnable: geni.IBoolean
    ColorTransformationMatrixFactor: geni.IFloat
    ColorTransformationMatrixFactorRaw: geni.IInteger
    ColorTransformationSelector: geni.IEnumeration
    ColorTransformationValue: geni.IFloat
    ColorTransformationValueRaw: geni.IInteger
    ColorTransformationValueSelector: geni.IEnumeration
    ComponentEnable: geni.IBoolean
    ComponentSelector: geni.IEnumeration
    ConfidenceThreshold: geni.IInteger
    CounterDuration: geni.IInteger
    CounterEventActivation: geni.IEnumeration
    CounterEventSource: geni.IEnumeration
    CounterReset: geni.ICommand
    CounterResetActivation: geni.IEnumeration
    CounterResetSource: geni.IEnumeration
    CounterSelector: geni.IEnumeration
    CounterStatus: geni.IEnumeration
    CounterTriggerActivation: geni.IEnumeration
    CounterTriggerSource: geni.IEnumeration
    CounterValue: geni.IInteger
    CriticalTemperature: geni.IBoolean
    CriticalTemperatureEventStreamChannelIndex: geni.IInteger
    CriticalTemperatureEventTimestamp: geni.IInteger
    CxpConnectionSelector: geni.IInteger
    CxpConnectionTestErrorCount: geni.IInteger
    CxpConnectionTestMode: geni.IEnumeration
    CxpConnectionTestPacketCount: geni.IInteger
    CxpErrorCounterReset: geni.ICommand
    CxpErrorCounterSelector: geni.IEnumeration
    CxpErrorCounterStatus: geni.IEnumeration
    CxpErrorCounterValue: geni.IInteger
    CxpLinkConfiguration: geni.IEnumeration
    CxpLinkConfigurationPreferred: geni.IEnumeration
    CxpLinkConfigurationStatus: geni.IEnumeration
    CxpSendReceiveSelector: geni.IEnumeration
    DecimationHorizontal: geni.IInteger
    DecimationVertical: geni.IInteger
    DefectPixelCorrectionMode: geni.IEnumeration
    DemosaicingMode: geni.IEnumeration
    DepthMax: geni.IInteger
    DepthMin: geni.IInteger
    DeviceCharacterSet: geni.IEnumeration
    DeviceColorPipelineVersion: geni.IInteger
    DeviceEventChannelCount: geni.IInteger
    DeviceFamilyName: geni.IString
    DeviceFeaturePersistenceEnd: geni.ICommand
    DeviceFeaturePersistenceStart: geni.ICommand
    DeviceFirmwareVersion: geni.IString
    DeviceGenCPVersionMajor: geni.IInteger
    DeviceGenCPVersionMinor: geni.IInteger
    DeviceID: geni.IString
    DeviceIndicatorMode: geni.IEnumeration
    DeviceLinkConnectionCount: geni.IInteger
    DeviceLinkCurrentThroughput: geni.IInteger
    DeviceLinkSelector: geni.IInteger
    DeviceLinkSpeed: geni.IInteger
    DeviceLinkThroughputLimit: geni.IInteger
    DeviceLinkThroughputLimitMode: geni.IEnumeration
    DeviceManifestPrimaryURL: geni.IString
    DeviceManifestSchemaMajorVersion: geni.IInteger
    DeviceManifestSchemaMinorVersion: geni.IInteger
    DeviceManifestXMLMajorVersion: geni.IInteger
    DeviceManifestXMLMinorVersion: geni.IInteger
    DeviceManifestXMLSubMinorVersion: geni.IInteger
    DeviceManufacturerInfo: geni.IString
    DeviceModelName: geni.IString
    DeviceRegistersEndianness: geni.IEnumeration
    DeviceRegistersStreamingEnd: geni.ICommand
    DeviceRegistersStreamingStart: geni.ICommand
    DeviceReset: geni.ICommand
    DeviceSFNCVersionMajor: geni.IInteger
    DeviceSFNCVersionMinor: geni.IInteger
    DeviceSFNCVersionSubMinor: geni.IInteger
    DeviceScanType: geni.IEnumeration
    DeviceSerialNumber: geni.IString
    DeviceStreamChannelCount: geni.IInteger
    DeviceTLType: geni.IEnumeration
    DeviceTLVersionMajor: geni.IInteger
    DeviceTLVersionMinor: geni.IInteger
    DeviceTLVersionSubMinor: geni.IInteger
    DeviceTapGeometry: geni.IEnumeration
    DeviceTemperature: geni.IFloat
    DeviceTemperatureSelector: geni.IEnumeration
    DeviceType: geni.IEnumeration
    DeviceUserID: geni.IString
    DeviceVendorName: geni.IString
    DeviceVersion: geni.IString
    DigitalShift: geni.IInteger
    EnableBurstAcquisition: geni.IBoolean
    EventActionLate: geni.IInteger
    EventActionLateTimestamp: geni.IInteger
    EventCriticalTemperature: geni.IInteger
    EventCriticalTemperatureTimestamp: geni.IInteger
    EventExposureEnd: geni.IInteger
    EventExposureEndFrameID: geni.IInteger
    EventExposureEndTimestamp: geni.IInteger
    EventFrameBufferOverrun: geni.IInteger
    EventFrameBufferOverrunTimestamp: geni.IInteger
    EventFrameBurstStart: geni.IInteger
    EventFrameBurstStartFrameID: geni.IInteger
    EventFrameBurstStartOvertrigger: geni.IInteger
    EventFrameBurstStartOvertriggerFrameID: geni.IInteger
    EventFrameBurstStartOvertriggerTimestamp: geni.IInteger
    EventFrameBurstStartTimestamp: geni.IInteger
    EventFrameBurstStartWait: geni.IInteger
    EventFrameBurstStartWaitTimestamp: geni.IInteger
    EventFrameStart: geni.IInteger
    EventFrameStartFrameID: geni.IInteger
    EventFrameStartOvertrigger: geni.IInteger
    EventFrameStartOvertriggerFrameID: geni.IInteger
    EventFrameStartOvertriggerTimestamp: geni.IInteger
    EventFrameStartTimestamp: geni.IInteger
    EventFrameStartWait: geni.IInteger
    EventFrameStartWaitTimestamp: geni.IInteger
    EventFrameTriggerMissed: geni.IInteger
    EventFrameTriggerMissedTimestamp: geni.IInteger
    EventNotification: geni.IEnumeration
    EventOverTemperature: geni.IInteger
    EventOverTemperatureTimestamp: geni.IInteger
    EventOverrun: geni.IInteger
    EventOverrunEventFrameID: geni.IInteger
    EventOverrunEventStreamChannelIndex: geni.IInteger
    EventOverrunEventTimestamp: geni.IInteger
    EventOverrunTimestamp: geni.IInteger
    EventSelector: geni.IEnumeration
    EventTemperatureStatusChanged: geni.IInteger
    EventTemperatureStatusChangedStatus: geni.IEnumeration
    EventTemperatureStatusChangedTimestamp: geni.IInteger
    EventTest: geni.IInteger
    EventTestTimestamp: geni.IInteger
    ExpertFeatureAccessKey: geni.IInteger
    ExpertFeatureAccessSelector: geni.IEnumeration
    ExpertFeatureEnable: geni.IBoolean
    ExposureAuto: geni.IEnumeration
    ExposureEndEventFrameID: geni.IInteger
    ExposureEndEventStreamChannelIndex: geni.IInteger
    ExposureEndEventTimestamp: geni.IInteger
    ExposureMode: geni.IEnumeration
    ExposureOverlapTimeMax: geni.IFloat
    ExposureOverlapTimeMaxAbs: geni.IFloat
    ExposureOverlapTimeMaxRaw: geni.IInteger
    ExposureOverlapTimeMode: geni.IEnumeration
    ExposureStartDelayAbs: geni.IFloat
    ExposureStartDelayRaw: geni.IInteger
    ExposureTime: geni.IFloat
    ExposureTimeAbs: geni.IFloat
    ExposureTimeBaseAbs: geni.IFloat
    ExposureTimeBaseAbsEnable: geni.IBoolean
    ExposureTimeMode: geni.IEnumeration
    ExposureTimeRaw: geni.IInteger
    FastMode: geni.IBoolean
    FeatureSet: geni.IEnumeration
    FieldOutputMode: geni.IEnumeration
    FileAccessBuffer: geni.IRegister
    FileAccessLength: geni.IInteger
    FileAccessOffset: geni.IInteger
    FileOpenMode: geni.IEnumeration
    FileOperationExecute: geni.ICommand
    FileOperationResult: geni.IInteger
    FileOperationSelector: geni.IEnumeration
    FileOperationStatus: geni.IEnumeration
    FileSelector: geni.IEnumeration
    FileSize: geni.IInteger
    FilterSpatial: geni.IBoolean
    FilterStrength: geni.IInteger
    FilterTemporal: geni.IBoolean
    ForceFailedBuffer: geni.ICommand
    ForceFailedBufferCount: geni.IInteger
    FrameDuration: geni.IInteger
    FrameStartEventStreamChannelIndex: geni.IInteger
    FrameStartEventTimestamp: geni.IInteger
    FrameStartOvertriggerEventStreamChannelIndex: geni.IInteger
    FrameStartOvertriggerEventTimestamp: geni.IInteger
    FrameStartWaitEventStreamChannelIndex: geni.IInteger
    FrameStartWaitEventTimestamp: geni.IInteger
    FrameTimeoutAbs: geni.IFloat
    FrameTimeoutEnable: geni.IBoolean
    FrameTimeoutEventStreamChannelIndex: geni.IInteger
    FrameTimeoutEventTimestamp: geni.IInteger
    FrameWaitEventStreamChannelIndex: geni.IInteger
    FrameWaitEventTimestamp: geni.IInteger
    FrequencyConverterInputSource: geni.IEnumeration
    FrequencyConverterMultiplier: geni.IInteger
    FrequencyConverterPostDivider: geni.IInteger
    FrequencyConverterPreDivider: geni.IInteger
    FrequencyConverterPreventOvertrigger: geni.IBoolean
    FrequencyConverterSignalAlignment: geni.IEnumeration
    Gain: geni.IFloat
    GainAbs: geni.IFloat
    GainAuto: geni.IEnumeration
    GainRaw: geni.IInteger
    GainSelector: geni.IEnumeration
    Gamma: geni.IFloat
    GammaCorrection: geni.IBoolean
    GammaEnable: geni.IBoolean
    GammaSelector: geni.IEnumeration
    GenDCStreamingMode: geni.IEnumeration
    GenDCStreamingStatus: geni.IEnumeration
    GevCCP: geni.IEnumeration
    GevCurrentDefaultGateway: geni.IInteger
    GevCurrentIPAddress: geni.IInteger
    GevCurrentIPConfiguration: geni.IInteger
    GevCurrentIPConfigurationDHCP: geni.IBoolean
    GevCurrentIPConfigurationLLA: geni.IBoolean
    GevCurrentIPConfigurationPersistentIP: geni.IBoolean
    GevCurrentSubnetMask: geni.IInteger
    GevDeviceModeCharacterSet: geni.IInteger
    GevDeviceModeIsBigEndian: geni.IBoolean
    GevFirstURL: geni.IString
    GevGVSPExtendedIDMode: geni.IEnumeration
    GevHeartbeatTimeout: geni.IInteger
    GevIEEE1588: geni.IBoolean
    GevIEEE1588ClockId: geni.IInteger
    GevIEEE1588DataSetLatch: geni.ICommand
    GevIEEE1588OffsetFromMaster: geni.IInteger
    GevIEEE1588ParentClockId: geni.IInteger
    GevIEEE1588Status: geni.IEnumeration
    GevIEEE1588StatusLatched: geni.IEnumeration
    GevInterfaceSelector: geni.IEnumeration
    GevLinkCrossover: geni.IBoolean
    GevLinkFullDuplex: geni.IBoolean
    GevLinkMaster: geni.IBoolean
    GevLinkSpeed: geni.IInteger
    GevMACAddress: geni.IInteger
    GevMessageChannelCount: geni.IInteger
    GevNumberOfInterfaces: geni.IInteger
    GevPTPDiagnosticsQueueRxEvntMaxNumElements: geni.IInteger
    GevPTPDiagnosticsQueueRxEvntPushNumFailure: geni.IInteger
    GevPTPDiagnosticsQueueRxGnrlMaxNumElements: geni.IInteger
    GevPTPDiagnosticsQueueRxGnrlPushNumFailure: geni.IInteger
    GevPTPDiagnosticsQueueSendNumFailure: geni.IInteger
    GevPersistentDefaultGateway: geni.IInteger
    GevPersistentIPAddress: geni.IInteger
    GevPersistentSubnetMask: geni.IInteger
    GevSCBWA: geni.IInteger
    GevSCBWR: geni.IInteger
    GevSCBWRA: geni.IInteger
    GevSCDA: geni.IInteger
    GevSCDCT: geni.IInteger
    GevSCDMT: geni.IInteger
    GevSCFJM: geni.IInteger
    GevSCFTD: geni.IInteger
    GevSCPD: geni.IInteger
    GevSCPHostPort: geni.IInteger
    GevSCPInterfaceIndex: geni.IInteger
    GevSCPSBigEndian: geni.IBoolean
    GevSCPSDoNotFragment: geni.IBoolean
    GevSCPSFireTestPacket: geni.ICommand
    GevSCPSPacketSize: geni.IInteger
    GevSecondURL: geni.IString
    GevStreamChannelCount: geni.IInteger
    GevStreamChannelSelector: geni.IEnumeration
    GevSupportedIEEE1588: geni.IBoolean
    GevSupportedIPConfigurationDHCP: geni.IBoolean
    GevSupportedIPConfigurationLLA: geni.IBoolean
    GevSupportedIPConfigurationPersistentIP: geni.IBoolean
    GevSupportedOptionalCommandsConcatenation: geni.IBoolean
    GevSupportedOptionalCommandsEVENT: geni.IBoolean
    GevSupportedOptionalCommandsEVENTDATA: geni.IBoolean
    GevSupportedOptionalCommandsPACKETRESEND: geni.IBoolean
    GevSupportedOptionalCommandsWRITEMEM: geni.IBoolean
    GevSupportedOptionalLegacy16BitBlockID: geni.IBoolean
    GevTimestampControlLatch: geni.ICommand
    GevTimestampControlLatchReset: geni.ICommand
    GevTimestampControlReset: geni.ICommand
    GevTimestampTickFrequency: geni.IInteger
    GevTimestampValue: geni.IInteger
    GevVersionMajor: geni.IInteger
    GevVersionMinor: geni.IInteger
    GrayValueAdjustmentDampingAbs: geni.IFloat
    GrayValueAdjustmentDampingRaw: geni.IInteger
    Height: geni.IInteger
    HeightMax: geni.IInteger
    Image1StreamID: geni.IInteger
    ImageCompressionMode: geni.IEnumeration
    ImageCompressionRateOption: geni.IEnumeration
    ImageFileMode: geni.IEnumeration
    ImageFilename: geni.IString
    IntensityCalculation: geni.IEnumeration
    InterlacedIntegrationMode: geni.IEnumeration
    LUTEnable: geni.IBoolean
    LUTIndex: geni.IInteger
    LUTSelector: geni.IEnumeration
    LUTValue: geni.IInteger
    LUTValueAll: geni.IRegister
    LastError: geni.IEnumeration
    LateActionEventStreamChannelIndex: geni.IInteger
    LateActionEventTimestamp: geni.IInteger
    LegacyBinningVertical: geni.IEnumeration
    LightSourcePreset: geni.IEnumeration
    LightSourceSelector: geni.IEnumeration
    Line1RisingEdgeEventStreamChannelIndex: geni.IInteger
    Line1RisingEdgeEventTimestamp: geni.IInteger
    Line2RisingEdgeEventStreamChannelIndex: geni.IInteger
    Line2RisingEdgeEventTimestamp: geni.IInteger
    Line3RisingEdgeEventStreamChannelIndex: geni.IInteger
    Line3RisingEdgeEventTimestamp: geni.IInteger
    Line4RisingEdgeEventStreamChannelIndex: geni.IInteger
    Line4RisingEdgeEventTimestamp: geni.IInteger
    LineDebouncerTime: geni.IFloat
    LineDebouncerTimeAbs: geni.IFloat
    LineFormat: geni.IEnumeration
    LineInverter: geni.IBoolean
    LineLogic: geni.IEnumeration
    LineMinimumOutputPulseWidth: geni.IFloat
    LineMode: geni.IEnumeration
    LineOverloadReset: geni.ICommand
    LineOverloadStatus: geni.IBoolean
    LinePitch: geni.IInteger
    LinePitchEnable: geni.IBoolean
    LineSelector: geni.IEnumeration
    LineSource: geni.IEnumeration
    LineStartOvertriggerEventStreamChannelIndex: geni.IInteger
    LineStartOvertriggerEventTimestamp: geni.IInteger
    LineStatus: geni.IBoolean
    LineStatusAll: geni.IInteger
    LineTermination: geni.IBoolean
    MinOutPulseWidthAbs: geni.IFloat
    MultiCameraChannel: geni.IInteger
    NoiseReduction: geni.IFloat
    NoiseReductionAbs: geni.IFloat
    NoiseReductionRaw: geni.IInteger
    NumberOfActionSignals: geni.IInteger
    OffsetX: geni.IInteger
    OffsetY: geni.IInteger
    OperatingMode: geni.IEnumeration
    OutlierRemoval: geni.IBoolean
    OverTemperature: geni.IBoolean
    OverTemperatureEventStreamChannelIndex: geni.IInteger
    OverTemperatureEventTimestamp: geni.IInteger
    OverlapMode: geni.IEnumeration
    ParameterSelector: geni.IEnumeration
    PayloadFinalTransfer1Size: geni.IInteger
    PayloadFinalTransfer2Size: geni.IInteger
    PayloadSize: geni.IInteger
    PayloadTransferBlockDelay: geni.IInteger
    PayloadTransferCount: geni.IInteger
    PayloadTransferSize: geni.IInteger
    PgiMode: geni.IEnumeration
    PixelCoding: geni.IEnumeration
    PixelColorFilter: geni.IEnumeration
    PixelDynamicRangeMax: geni.IInteger
    PixelDynamicRangeMin: geni.IInteger
    PixelFormat: geni.IEnumeration
    PixelFormatLegacy: geni.IBoolean
    PixelSize: geni.IEnumeration
    Prelines: geni.IInteger
    ProcessedRawEnable: geni.IBoolean
    PtpClockAccuracy: geni.IEnumeration
    PtpClockID: geni.IInteger
    PtpDataSetLatch: geni.ICommand
    PtpEnable: geni.IBoolean
    PtpGrandmasterClockID: geni.IInteger
    PtpOffsetFromMaster: geni.IInteger
    PtpParentClockID: geni.IInteger
    PtpServoStatus: geni.IEnumeration
    PtpStatus: geni.IEnumeration
    ROIZoneMode: geni.IEnumeration
    ROIZoneOffset: geni.IInteger
    ROIZoneSelector: geni.IEnumeration
    ROIZoneSize: geni.IInteger
    ReadoutTime: geni.IInteger
    ReadoutTimeAbs: geni.IFloat
    RemoveLimits: geni.IBoolean
    RemoveParameterLimit: geni.IBoolean
    RemoveParameterLimitSelector: geni.IEnumeration
    ResetTime: geni.IInteger
    ResultingFramePeriodAbs: geni.IFloat
    ResultingFrameRate: geni.IFloat
    ResultingFrameRateAbs: geni.IFloat
    ResultingLinePeriodAbs: geni.IFloat
    ResultingLineRateAbs: geni.IFloat
    ReverseX: geni.IBoolean
    ReverseY: geni.IBoolean
    SIPayloadFinalTransfer1Size: geni.IInteger
    SIPayloadFinalTransfer2Size: geni.IInteger
    SIPayloadTransferCount: geni.IInteger
    SIPayloadTransferSize: geni.IInteger
    ScalingHorizontal: geni.IFloat
    ScalingHorizontalAbs: geni.IFloat
    ScalingVertical: geni.IFloat
    ScalingVerticalAbs: geni.IFloat
    Scan3dAxisMax: geni.IFloat
    Scan3dAxisMin: geni.IFloat
    Scan3dCalibrationOffset: geni.IFloat
    Scan3dCoordinateOffset: geni.IFloat
    Scan3dCoordinateScale: geni.IFloat
    Scan3dCoordinateSelector: geni.IEnumeration
    Scan3dCoordinateSystem: geni.IEnumeration
    Scan3dCoordinateSystemReference: geni.IEnumeration
    Scan3dDistanceUnit: geni.IEnumeration
    Scan3dFocalLength: geni.IFloat
    Scan3dInvalidDataFlag: geni.IBoolean
    Scan3dInvalidDataValue: geni.IFloat
    Scan3dOutputMode: geni.IEnumeration
    Scan3dPrincipalPointU: geni.IFloat
    Scan3dPrincipalPointV: geni.IFloat
    SensorBitDepth: geni.IEnumeration
    SensorDigitizationTaps: geni.IEnumeration
    SensorHeight: geni.IInteger
    SensorPixelHeight: geni.IFloat
    SensorPixelWidth: geni.IFloat
    SensorPosition: geni.IFloat
    SensorReadoutMode: geni.IEnumeration
    SensorReadoutTime: geni.IFloat
    SensorShutterMode: geni.IEnumeration
    SensorWidth: geni.IInteger
    SequenceAddressBitSelector: geni.IEnumeration
    SequenceAddressBitSource: geni.IEnumeration
    SequenceAdvanceMode: geni.IEnumeration
    SequenceAsyncAdvance: geni.ICommand
    SequenceAsyncRestart: geni.ICommand
    SequenceConfigurationMode: geni.IEnumeration
    SequenceControlSelector: geni.IEnumeration
    SequenceControlSource: geni.IEnumeration
    SequenceCurrentSet: geni.IInteger
    SequenceEnable: geni.IBoolean
    SequenceSetExecutions: geni.IInteger
    SequenceSetIndex: geni.IInteger
    SequenceSetLoad: geni.ICommand
    SequenceSetStore: geni.ICommand
    SequenceSetTotalNumber: geni.IInteger
    SequencerConfigurationMode: geni.IEnumeration
    SequencerMode: geni.IEnumeration
    SequencerPathSelector: geni.IInteger
    SequencerSetActive: geni.IInteger
    SequencerSetLoad: geni.ICommand
    SequencerSetNext: geni.IInteger
    SequencerSetSave: geni.ICommand
    SequencerSetSelector: geni.IInteger
    SequencerSetStart: geni.IInteger
    SequencerTriggerActivation: geni.IEnumeration
    SequencerTriggerSource: geni.IEnumeration
    ShadingEnable: geni.IBoolean
    ShadingSelector: geni.IEnumeration
    ShadingSetActivate: geni.ICommand
    ShadingSetCreate: geni.IEnumeration
    ShadingSetDefaultSelector: geni.IEnumeration
    ShadingSetSelector: geni.IEnumeration
    ShadingStatus: geni.IEnumeration
    ShaftEncoderModuleCounter: geni.IInteger
    ShaftEncoderModuleCounterMax: geni.IInteger
    ShaftEncoderModuleCounterMode: geni.IEnumeration
    ShaftEncoderModuleCounterReset: geni.ICommand
    ShaftEncoderModuleLineSelector: geni.IEnumeration
    ShaftEncoderModuleLineSource: geni.IEnumeration
    ShaftEncoderModuleMode: geni.IEnumeration
    ShaftEncoderModuleReverseCounterMax: geni.IInteger
    ShaftEncoderModuleReverseCounterReset: geni.ICommand
    SharpnessEnhancement: geni.IFloat
    SharpnessEnhancementAbs: geni.IFloat
    SharpnessEnhancementRaw: geni.IInteger
    ShutterMode: geni.IEnumeration
    SoftwareSignalPulse: geni.ICommand
    SoftwareSignalSelector: geni.IEnumeration
    SpatialCorrection: geni.IInteger
    StackedZoneImagingEnable: geni.IBoolean
    StackedZoneImagingIndex: geni.IInteger
    StackedZoneImagingZoneEnable: geni.IBoolean
    StackedZoneImagingZoneHeight: geni.IInteger
    StackedZoneImagingZoneOffsetY: geni.IInteger
    StartupTime: geni.IInteger
    SubstrateVoltage: geni.IInteger
    SyncFreeRunTimerEnable: geni.IBoolean
    SyncFreeRunTimerStartTimeHigh: geni.IInteger
    SyncFreeRunTimerStartTimeLow: geni.IInteger
    SyncFreeRunTimerTriggerRateAbs: geni.IFloat
    SyncFreeRunTimerUpdate: geni.ICommand
    SyncUserOutputSelector: geni.IEnumeration
    SyncUserOutputValue: geni.IBoolean
    SyncUserOutputValueAll: geni.IInteger
    TemperatureAbs: geni.IFloat
    TemperatureSelector: geni.IEnumeration
    TemperatureState: geni.IEnumeration
    TestEventGenerate: geni.ICommand
    TestImageResetAndHold: geni.IBoolean
    TestImageSelector: geni.IEnumeration
    TestPattern: geni.IEnumeration
    TestPendingAck: geni.IInteger
    ThermalDriftCorrection: geni.IBoolean
    TimerDelay: geni.IFloat
    TimerDelayAbs: geni.IFloat
    TimerDelayRaw: geni.IInteger
    TimerDelayTimebaseAbs: geni.IFloat
    TimerDuration: geni.IFloat
    TimerDurationAbs: geni.IFloat
    TimerDurationRaw: geni.IInteger
    TimerDurationTimebaseAbs: geni.IFloat
    TimerReset: geni.ICommand
    TimerSelector: geni.IEnumeration
    TimerSequenceCurrentEntryIndex: geni.IInteger
    TimerSequenceEnable: geni.IBoolean
    TimerSequenceEntrySelector: geni.IEnumeration
    TimerSequenceLastEntryIndex: geni.IInteger
    TimerSequenceTimerDelayRaw: geni.IInteger
    TimerSequenceTimerDurationRaw: geni.IInteger
    TimerSequenceTimerEnable: geni.IBoolean
    TimerSequenceTimerInverter: geni.IBoolean
    TimerSequenceTimerSelector: geni.IEnumeration
    TimerStatus: geni.IEnumeration
    TimerTriggerActivation: geni.IEnumeration
    TimerTriggerArmDelay: geni.IFloat
    TimerTriggerSource: geni.IEnumeration
    TimestampLatch: geni.ICommand
    TimestampLatchValue: geni.IInteger
    TimestampReset: geni.ICommand
    TonalRangeAuto: geni.IEnumeration
    TonalRangeEnable: geni.IEnumeration
    TonalRangeSelector: geni.IEnumeration
    TonalRangeSourceBright: geni.IInteger
    TonalRangeSourceDark: geni.IInteger
    TonalRangeTargetBright: geni.IInteger
    TonalRangeTargetDark: geni.IInteger
    TriggerActivation: geni.IEnumeration
    TriggerControlImplementation: geni.IEnumeration
    TriggerDelay: geni.IFloat
    TriggerDelayAbs: geni.IFloat
    TriggerDelayLineTriggerCount: geni.IInteger
    TriggerDelaySource: geni.IEnumeration
    TriggerMode: geni.IEnumeration
    TriggerPartialClosingFrame: geni.IBoolean
    TriggerSelector: geni.IEnumeration
    TriggerSoftware: geni.ICommand
    TriggerSource: geni.IEnumeration
    UserDefinedValue: geni.IInteger
    UserDefinedValueSelector: geni.IEnumeration
    UserOutputSelector: geni.IEnumeration
    UserOutputValue: geni.IBoolean
    UserOutputValueAll: geni.IInteger
    UserOutputValueAllMask: geni.IInteger
    UserSetDefault: geni.IEnumeration
    UserSetDefaultSelector: geni.IEnumeration
    UserSetLoad: geni.ICommand
    UserSetSave: geni.ICommand
    UserSetSelector: geni.IEnumeration
    VInpBitLength: geni.IInteger
    VInpSamplingPoint: geni.IInteger
    VInpSignalReadoutActivation: geni.IEnumeration
    VInpSignalSource: geni.IEnumeration
    VignettingCorrectionLoad: geni.ICommand
    VignettingCorrectionMode: geni.IEnumeration
    VirtualLine1RisingEdgeEventStreamChannelIndex: geni.IInteger
    VirtualLine1RisingEdgeEventTimestamp: geni.IInteger
    VirtualLine2RisingEdgeEventStreamChannelIndex: geni.IInteger
    VirtualLine2RisingEdgeEventTimestamp: geni.IInteger
    VirtualLine3RisingEdgeEventStreamChannelIndex: geni.IInteger
    VirtualLine3RisingEdgeEventTimestamp: geni.IInteger
    VirtualLine4RisingEdgeEventStreamChannelIndex: geni.IInteger
    VirtualLine4RisingEdgeEventTimestamp: geni.IInteger
    VolatileColumnOffsetEnable: geni.IBoolean
    VolatileColumnOffsetIndex: geni.IInteger
    VolatileColumnOffsetValue: geni.IInteger
    VolatileRowOffsetEnable: geni.IBoolean
    VolatileRowOffsetIndex: geni.IInteger
    VolatileRowOffsetValue: geni.IInteger
    Width: geni.IInteger
    WidthMax: geni.IInteger
    WorkingRangeMax: geni.IInteger
    WorkingRangeMin: geni.IInteger
    ZOffsetOriginToCameraFront: geni.IFloat

class ChunkDataParams:
    BslChunkAutoBrightnessStatus: geni.IEnumeration
    BslChunkTimestampSelector: geni.IEnumeration
    BslChunkTimestampValue: geni.IInteger
    ChunkCounterSelector: geni.IEnumeration
    ChunkCounterValue: geni.IInteger
    ChunkDynamicRangeMax: geni.IInteger
    ChunkDynamicRangeMin: geni.IInteger
    ChunkExposureTime: geni.IFloat
    ChunkFrameID: geni.IInteger
    ChunkFrameTriggerCounter: geni.IInteger
    ChunkFrameTriggerIgnoredCounter: geni.IInteger
    ChunkFramecounter: geni.IInteger
    ChunkFramesPerTriggerCounter: geni.IInteger
    ChunkGain: geni.IFloat
    ChunkGainAll: geni.IInteger
    ChunkGainSelector: geni.IEnumeration
    ChunkHeight: geni.IInteger
    ChunkInputStatusAtLineTriggerBitsPerLine: geni.IInteger
    ChunkInputStatusAtLineTriggerIndex: geni.IInteger
    ChunkInputStatusAtLineTriggerValue: geni.IInteger
    ChunkLineStatusAll: geni.IInteger
    ChunkLineTriggerCounter: geni.IInteger
    ChunkLineTriggerEndToEndCounter: geni.IInteger
    ChunkLineTriggerIgnoredCounter: geni.IInteger
    ChunkOffsetX: geni.IInteger
    ChunkOffsetY: geni.IInteger
    ChunkPayloadCRC16: geni.IInteger
    ChunkPixelFormat: geni.IEnumeration
    ChunkSequenceSetIndex: geni.IInteger
    ChunkSequencerSetActive: geni.IInteger
    ChunkShaftEncoderCounter: geni.IInteger
    ChunkStride: geni.IInteger
    ChunkTimestamp: geni.IInteger
    ChunkTriggerinputcounter: geni.IInteger
    ChunkVirtLineStatusAll: geni.IInteger
    ChunkWidth: geni.IInteger

class GrabResult(ChunkDataParams):
    def Release(self) -> None: ...
    def IsUnique(self) -> bool: ...
    def IsValid(self) -> bool: ...
    def GetImageFormat(self) -> int: ...
    def GetArray(self) -> np.ndarray: ...
    def GetChunkNode(self, nodeName: str) -> geni.IValue: ...
    def GetArrayZeroCopy(self, raw: bool = ...) -> Generator[None, None, None]: ...
    def GrabSucceeded(self) -> bool: ...
    def GetErrorDescription(self) -> "str": ...
    def GetErrorCode(self) -> int: ...
    def GetPayloadType(self) -> int: ...
    def GetPixelType(self) -> int: ...
    def GetWidth(self) -> int: ...
    def GetHeight(self) -> int: ...
    def GetOffsetX(self) -> int: ...
    def GetOffsetY(self) -> int: ...
    def GetPaddingX(self) -> int: ...
    def GetPaddingY(self) -> int: ...
    def GetPayloadSize(self) -> int: ...
    def GetBufferSize(self) -> int: ...
    def GetBlockID(self) -> int: ...
    def GetTimeStamp(self) -> int: ...
    def GetStride(self) -> int: ...
    def GetImageSize(self) -> int: ...
    def GetCameraContext(self) -> int: ...
    def GetID(self) -> int: ...
    def GetImageNumber(self) -> int: ...
    def GetNumberOfSkippedImages(self) -> int: ...
    def IsChunkDataAvailable(self) -> bool: ...
    def GetChunkDataNodeMap(self) -> geni.INodeMap: ...
    def HasCRC(self) -> bool: ...
    def CheckCRC(self) -> bool: ...
    def GetBufferContext(self) -> int: ...
    def GetBuffer(self) -> bytes: ...
    def GetImageBuffer(self) -> bytes: ...
    def GetMemoryView(self) -> bytes: ...
    def GetImageMemoryView(self) -> bytes: ...
    def __enter__(self): ...
    def __exit__(self, type, value, traceback) -> None: ...

    Width: int
    Height: int
    PixelType: int
    Array: np.ndarray
    ErrorCode: int
    ErrorDescription: str

GrabStrategy_OneByOne: int
GrabStrategy_LatestImageOnly: int
GrabStrategy_LatestImages: int
GrabStrategy_UpcomingImage: int
GrabLoop_ProvidedByInstantCamera: int
GrabLoop_ProvidedByUser: int
CameraEventAvailability_Mandatory: int
CameraEventAvailability_Optional: int
TimeoutHandling_Return: int
TimeoutHandling_ThrowException: int

RegistrationMode_Append: int
RegistrationMode_ReplaceAll: int
Cleanup_None: int
Cleanup_Delete: int

PYLON_VERSION_MAJOR: int
PYLON_VERSION_MINOR: int
PYLON_VERSION_SUBMINOR: int
PYLON_VERSION_BUILD: int
PYLON_VERSIONSTRING_MAJOR: int
PYLON_VERSIONSTRING_MINOR: int
PYLON_VERSIONSTRING_SUBMINOR: int
PYLON_VERSIONSTRING_BUILD: int
PYLON_VERSIONSTRING_EXTENSION: int
GenericException: int
BadAllocException: int
InvalidArgumentException: int
OutOfRangeException: int
PropertyException: int
RuntimeException: int
LogicalErrorException: int
AccessException: int
TimeoutException: int
DynamicCastException: int
PIXEL_MONO: int
PIXEL_COLOR: int
PIXEL_CUSTOMTYPE: int
PixelType_Undefined: int
PixelType_Mono1packed: int
PixelType_Mono2packed: int
PixelType_Mono4packed: int
PixelType_Mono8: int
PixelType_Mono8signed: int
PixelType_Mono10: int
PixelType_Mono10packed: int
PixelType_Mono10p: int
PixelType_Mono12: int
PixelType_Mono12packed: int
PixelType_Mono12p: int
PixelType_Mono16: int
PixelType_BayerGR8: int
PixelType_BayerRG8: int
PixelType_BayerGB8: int
PixelType_BayerBG8: int
PixelType_BayerGR10: int
PixelType_BayerRG10: int
PixelType_BayerGB10: int
PixelType_BayerBG10: int
PixelType_BayerGR12: int
PixelType_BayerRG12: int
PixelType_BayerGB12: int
PixelType_BayerBG12: int
PixelType_RGB8packed: int
PixelType_BGR8packed: int
PixelType_RGBA8packed: int
PixelType_BGRA8packed: int
PixelType_RGB10packed: int
PixelType_BGR10packed: int
PixelType_RGB12packed: int
PixelType_BGR12packed: int
PixelType_RGB16packed: int
PixelType_BGR10V1packed: int
PixelType_BGR10V2packed: int
PixelType_YUV411packed: int
PixelType_YUV422packed: int
PixelType_YUV444packed: int
PixelType_RGB8planar: int
PixelType_RGB10planar: int
PixelType_RGB12planar: int
PixelType_RGB16planar: int
PixelType_YUV422_YUYV_Packed: int
PixelType_YUV444planar: int
PixelType_YUV422planar: int
PixelType_YUV420planar: int
PixelType_YCbCr420_8_YY_CbCr_Semiplanar: int
PixelType_YCbCr422_8_YY_CbCr_Semiplanar: int
PixelType_BayerGR12Packed: int
PixelType_BayerRG12Packed: int
PixelType_BayerGB12Packed: int
PixelType_BayerBG12Packed: int
PixelType_BayerGR10p: int
PixelType_BayerRG10p: int
PixelType_BayerGB10p: int
PixelType_BayerBG10p: int
PixelType_BayerGR12p: int
PixelType_BayerRG12p: int
PixelType_BayerGB12p: int
PixelType_BayerBG12p: int
PixelType_BayerGR16: int
PixelType_BayerRG16: int
PixelType_BayerGB16: int
PixelType_BayerBG16: int
PixelType_RGB12V1packed: int
PixelType_Double: int
PixelType_Confidence8: int
PixelType_Confidence16: int
PixelType_Coord3D_C8: int
PixelType_Coord3D_C16: int
PixelType_Coord3D_ABC32f: int
PixelType_Data8: int
PixelType_Data8s: int
PixelType_Data16: int
PixelType_Data16s: int
PixelType_Data32: int
PixelType_Data32s: int
PixelType_Data64: int
PixelType_Data64s: int
PixelType_Data32f: int
PixelType_Data64f: int

class ConfigurationEventHandler:
    def __init__(self) -> None: ...
    def OnAttach(self, camera: InstantCamera) -> None: ...
    def OnAttached(self, camera: InstantCamera) -> None: ...
    def OnDetach(self, camera: InstantCamera) -> None: ...
    def OnDetached(self, camera: InstantCamera) -> None: ...
    def OnDestroy(self, camera: InstantCamera) -> None: ...
    def OnDestroyed(self, camera: InstantCamera) -> None: ...
    def OnOpen(self, camera: InstantCamera) -> None: ...
    def OnOpened(self, camera: InstantCamera) -> None: ...
    def OnClose(self, camera: InstantCamera) -> None: ...
    def OnClosed(self, camera: InstantCamera) -> None: ...
    def OnGrabStart(self, camera: InstantCamera) -> None: ...
    def OnGrabStarted(self, camera: InstantCamera) -> None: ...
    def OnGrabStop(self, camera: InstantCamera) -> None: ...
    def OnGrabStopped(self, camera: InstantCamera) -> None: ...
    def OnGrabError(
        self, camera: InstantCamera, errorMessage: "char const *"
    ) -> None: ...
    def OnCameraDeviceRemoved(self, camera: InstantCamera) -> None: ...
    def OnConfigurationRegistered(self, camera: InstantCamera) -> None: ...
    def OnConfigurationDeregistered(self, camera: InstantCamera) -> None: ...
    def DestroyConfiguration(self) -> None: ...

class CameraEventHandler:
    def __init__(self) -> None: ...
    def OnCameraEvent(
        self, camera: InstantCamera, userProvidedId: intptr_t, pNode: INode
    ) -> None: ...
    def OnCameraEventHandlerRegistered(
        self,
        camera: InstantCamera,
        nodeName: "Pylon::String_t const &",
        userProvidedId: intptr_t,
    ) -> None: ...
    def OnCameraEventHandlerDeregistered(
        self,
        camera: InstantCamera,
        nodeName: "Pylon::String_t const &",
        userProvidedId: intptr_t,
    ) -> None: ...
    def DestroyCameraEventHandler(self) -> None: ...

class ImageEventHandler:
    def __init__(self) -> None: ...
    def OnImagesSkipped(
        self, camera: InstantCamera, countOfSkippedImages: int
    ) -> None: ...
    def OnImageGrabbed(self, camera: InstantCamera, grabResult: GrabResult) -> None: ...

class StreamGrabberParams:
    AccessMode: geni.IEnumeration
    AutoPacketSize: geni.IBoolean
    DestinationAddr: geni.IString
    DestinationPort: geni.IInteger
    EnableResend: geni.IBoolean
    FirewallTraversalInterval: geni.IInteger
    FrameRetention: geni.IInteger
    MaxBufferSize: geni.IInteger
    MaxNumBuffer: geni.IInteger
    MaxTransferSize: geni.IInteger
    MaximumNumberResendRequests: geni.IInteger
    NumMaxQueuedUrbs: geni.IInteger
    PacketTimeout: geni.IInteger
    PayloadSize: geni.IInteger
    ProbePacketSize: geni.ICommand
    ReceiveThreadPriority: geni.IInteger
    ReceiveThreadPriorityOverride: geni.IBoolean
    ReceiveWindowSize: geni.IInteger
    ResendRequestBatching: geni.IInteger
    ResendRequestResponseTimeout: geni.IInteger
    ResendRequestThreshold: geni.IInteger
    ResendTimeout: geni.IInteger
    SocketBufferSize: geni.IInteger
    Statistic_Buffer_Underrun_Count: geni.IInteger
    Statistic_Failed_Buffer_Count: geni.IInteger
    Statistic_Failed_Packet_Count: geni.IInteger
    Statistic_Last_Block_Id: geni.IInteger
    Statistic_Last_Failed_Buffer_Status: geni.IInteger
    Statistic_Last_Failed_Buffer_Status_Text: geni.IString
    Statistic_Missed_Frame_Count: geni.IInteger
    Statistic_Out_Of_Memory_Error_Count: geni.IInteger
    Statistic_Resend_Packet_Count: geni.IInteger
    Statistic_Resend_Request_Count: geni.IInteger
    Statistic_Resynchronization_Count: geni.IInteger
    Statistic_Total_Buffer_Count: geni.IInteger
    Statistic_Total_Packet_Count: geni.IInteger
    Status: geni.IEnumeration
    StreamAnnounceBufferMinimum: geni.IInteger
    StreamAnnouncedBufferCount: geni.IInteger
    StreamBufferAlignment: geni.IInteger
    StreamBufferHandlingMode: geni.IEnumeration
    StreamChunkCountMaximum: geni.IInteger
    StreamDeliveredFrameCount: geni.IInteger
    StreamID: geni.IString
    StreamInputBufferCount: geni.IInteger
    StreamIsGrabbing: geni.IBoolean
    StreamLostFrameCount: geni.IInteger
    StreamOutputBufferCount: geni.IInteger
    StreamStartedFrameCount: geni.IInteger
    StreamType: geni.IEnumeration
    TransferLoopThreadPriority: geni.IInteger
    TransmissionType: geni.IEnumeration
    Type: geni.IEnumeration
    TypeIsSocketDriverAvailable: geni.IInteger
    TypeIsWindowsFilterDriverAvailable: geni.IInteger
    TypeIsWindowsIntelPerformanceDriverAvailable: geni.IInteger
    UseExtendedIdIfAvailable: geni.IBoolean

class InstantCameraParams:
    AcquisitionStartStopExecutionEnable: geni.IBoolean
    ChunkNodeMapsEnable: geni.IBoolean
    ClearBufferModeEnable: geni.IBoolean
    GrabCameraEvents: geni.IBoolean
    GrabLoopThreadPriority: geni.IInteger
    GrabLoopThreadPriorityOverride: geni.IBoolean
    GrabLoopThreadTimeout: geni.IInteger
    GrabLoopThreadUseTimeout: geni.IBoolean
    InternalGrabEngineThreadPriority: geni.IInteger
    InternalGrabEngineThreadPriorityOverride: geni.IBoolean
    MaxNumBuffer: geni.IInteger
    MaxNumGrabResults: geni.IInteger
    MaxNumQueuedBuffer: geni.IInteger
    MigrationModeActive: geni.IBoolean
    MonitorModeActive: geni.IBoolean
    NumEmptyBuffers: geni.IInteger
    NumQueuedBuffers: geni.IInteger
    NumReadyBuffers: geni.IInteger
    OutputQueueSize: geni.IInteger
    StaticChunkNodeMapPoolSize: geni.IInteger
    UseExtendedIdIfAvailable: geni.IBoolean

class InstantCamera(UniversalCameraFeatures, InstantCameraParams):
    def __init__(self, pylon_device: IPylonDevice) -> InstantCamera: ...
    def Open(self) -> None: ...
    def Close(self) -> None: ...
    def StartGrabbing(self, capture_mode: int = ..., grab_loop: int = ...) -> None: ...
    def StartGrabbingMax(
        self, img_count: int = ..., capture_mode: int = ..., grab_loop: int = ...
    ) -> None: ...
    def StopGrabbing(self) -> None: ...
    def RetrieveResult(
        self, timeout_ms: float, timeout_handling: int = ...
    ) -> GrabResult: ...
    def GrabOne(self, timeout_ms: float, timeout_handling: int = ...) -> GrabResult: ...
    def GetDeviceInfo(self) -> DeviceInfo: ...
    def RegisterImageEventHandler(
        self, pImageEventHandler: ImageEventHandler, mode: int, cleanupProcedure: int
    ) -> None: ...
    def RegisterCameraEventHandler(
        self, pImageEventHandler: CameraEventHandler, mode: int, cleanupProcedure: int
    ) -> None: ...
    def IsGrabbing(self) -> bool: ...
    def Attach(self, IPylonDevice) -> None: ...
    def IsPylonDeviceAttached(self) -> bool: ...
    def IsCameraDeviceRemoved(self) -> bool: ...
    def HasOwnership(self) -> bool: ...
    def DestroyDevice(self) -> None: ...
    def DetachDevice(self) -> IPylonDevice: ...
    def Open(self) -> bool: ...
    def IsOpen(self) -> bool: ...
    def Close(self) -> None: ...
    def IsGrabbing(self) -> bool: ...
    def GetQueuedBufferCount(self) -> int: ...
    def WaitForFrameTriggerReady(self, *args) -> bool: ...
    def ExecuteSoftwareTrigger(self) -> None: ...
    def SetCameraContext(self, context: int) -> None: ...
    def GetCameraContext(self) -> int: ...
    def GetDeviceInfo(self) -> DeviceInfo: ...
    def GetNodeMap(self) -> geni.INodeMap: ...
    def GetTLNodeMap(self) -> geni.INodeMap: ...
    def GetStreamGrabberNodeMap(self) -> geni.INodeMap: ...
    def GetEventGrabberNodeMap(self) -> geni.INodeMap: ...
    def GetInstantCameraNodeMap(self) -> geni.INodeMap: ...
    def Is1394(self) -> bool: ...
    def IsGigE(self) -> bool: ...
    def IsUsb(self) -> bool: ...
    def IsCameraLink(self) -> bool: ...
    def IsCxp(self) -> bool: ...
    # def GetSfncVersion(self) -> VersionInfo: ...
    def IsBcon(self) -> bool: ...

ImageFileFormat_Tiff: int
ImageFileFormat_Png: int
ImageFileFormat_Raw: int
ImageFileFormat_Dng: int

class PylonImageBase:
    def Save(
        self, imageFileFormat: int, filename: str, pOptions: int = ...
    ) -> None: ...
    def Load(self, filename: str) -> None: ...
    def CanSaveWithoutConversion(self, imageFileFormat: int) -> bool: ...

class PylonImage(PylonImageBase):
    @staticmethod
    def Create(pixel_format: int, width: int, height: int) -> PylonImage: ...
    def CopyImage(self, image: PylonImage) -> None: ...
    def AttachGrabResultBufferWithUserHints(self, grabResult: GrabResult) -> None: ...
    def AttachGrabResultBuffer(self, grabResult: GrabResult) -> None: ...
    def AttachUserBuffer(self, buffer: bytes) -> None: ...
    def IsValid(self) -> bool: ...
    def GetPixelType(self) -> int: ...
    def GetWidth(self) -> int: ...
    def GetHeight(self) -> int: ...
    def GetPaddingX(self) -> int: ...
    def GetOrientation(self) -> int: ...
    def GetImageSize(self) -> int: ...
    def IsUnique(self) -> bool: ...
    def GetStride(self) -> int: ...
    def IsSupportedPixelType(self, pixelType: int) -> bool: ...
    def IsAdditionalPaddingSupported(self) -> bool: ...
    def Reset(self) -> None: ...
    def Release(self) -> None: ...
    def IsUserBufferAttached(self) -> bool: ...
    def IsGrabResultBufferAttached(self) -> bool: ...
    def GetAllocatedBufferSize(self) -> int: ...
    def ChangePixelType(self, pixelType: int) -> None: ...
    def GetPlane(self, planeIndex: int) -> PylonImage: ...
    def GetAoi(
        self, topLeftX: int, topLeftY: int, width: int, height: int
    ) -> PylonImage: ...
    def GetBuffer(self) -> bytes: ...
    def GetImageFormat(self) -> int: ...
    def GetArray(self, raw: bool = ...) -> np.ndarray: ...

InconvertibleEdgeHandling_Clip: int
InconvertibleEdgeHandling_Extend: int
InconvertibleEdgeHandling_SetZero: int
MonoConversionMethod_Gamma: int
MonoConversionMethod_Truncate: int
OutputBitAlignment_LsbAligned: int
OutputBitAlignment_MsbAligned: int
OutputOrientation_BottomUp: int
OutputOrientation_TopDown: int
OutputOrientation_Unchanged: int

class ImageFormatConverterParams:
    AdditionalLeftShift: geni.IInteger
    Gamma: geni.IFloat
    InconvertibleEdgeHandling: geni.IEnumeration
    MonoConversionMethod: geni.IEnumeration
    OutputBitAlignment: geni.IEnumeration
    OutputOrientation: geni.IEnumeration
    OutputPaddingX: geni.IInteger

class ImageFormatConverter(ImageFormatConverterParams):
    def Initialize(self, sourcePixelType: int) -> None: ...
    def IsInitialized(self, sourcePixelType: int) -> bool: ...
    def Uninitialize(self) -> None: ...
    def GetBufferSizeForConversion(self) -> int: ...
    @staticmethod
    def IsSupportedInputFormat(sourcePixelType: int) -> bool: ...
    @staticmethod
    def IsSupportedOutputFormat(destinationPixelType: int) -> bool: ...
    def GetNodeMap(self) -> geni.geni.INodeMap: ...
    def Convert(self, grabResult: GrabResult) -> PylonImage: ...
    def ImageHasDestinationFormat(self, grabResult: GrabResult) -> bool: ...
    def SetOutputPixelFormat(self, pxl_fmt: int) -> None: ...
    def GetOutputPixelFormat(self) -> int: ...
    OutputPixelFormat: geni.IValue

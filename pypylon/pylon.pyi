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

    def SetBconAdapterLibraryName(self, BconAdapterLibraryNameValue: str) -> DeviceInfo: ...

    def IsBconAdapterLibraryNameAvailable(self) -> bool: ...

    def GetBconAdapterLibraryVersion(self) -> str: ...

    def SetBconAdapterLibraryVersion(self, BconAdapterLibraryVersionValue: str) -> DeviceInfo: ...

    def IsBconAdapterLibraryVersionAvailable(self) -> bool: ...

    def GetBconAdapterLibraryApiVersion(self) -> str: ...

    def SetBconAdapterLibraryApiVersion(self, BconAdapterLibraryApiVersionValue: str) -> DeviceInfo: ...

    def IsBconAdapterLibraryApiVersionAvailable(self) -> bool: ...

    def GetSupportedBconAdapterApiVersion(self) -> str: ...

    def SetSupportedBconAdapterApiVersion(self, SupportedBconAdapterApiVersionValue: str) -> DeviceInfo: ...

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

    def SetDeviceXMLFileOverride(self, DeviceXMLFileOverrideValue: str) -> DeviceInfo: ...

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

    def EnumerateDevices(self) -> List[DeviceInfo]: ...

    def CreateFirstDevice(self, di: DeviceInfo = ...) -> IPylonDevice: ...


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


class GrabResult:
    def Release(self) -> None: ...

    def IsUnique(self) -> bool: ...

    def GetImageFormat(self) -> int: ...

    def GetArray(self) -> np.ndarray: ...

    def GetChunkNode(self, nodeName: str) -> geni.IValue: ...

    def GetArrayZeroCopy(self, raw: bool = ...) -> Generator[None, None, None]: ...

    def GrabSucceeded(self) -> bool: ...

    def GetErrorDescription(self) -> 'str': ...

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


RegistrationMode_Append: int
RegistrationMode_ReplaceAll: int
Cleanup_None: int
Cleanup_Delete: int

class InstantCamera(UniversalCameraFeatures):
    def __init__(self, pylon_device: IPylonDevice) -> InstantCamera: ...
    def Open(self) -> None: ...
    def Close(self) -> None: ...
    def StartGrabbing(self) -> None: ...
    def StopGrabbing(self) -> None: ...
    def RetrieveResult(self, timeout_ms: float) -> GrabResult: ...
    def GetDeviceInfo(self) -> DeviceInfo: ...
    def RegisterImageEventHandler(self, pImageEventHandler: ImageEventHandler, mode: int,
                                  cleanupProcedure: int) -> None: ...

    def IsGrabbing(self) -> bool: ...


class ImageEventHandler:
    def OnImagesSkipped(self, camera: InstantCamera, countOfSkippedImages: int) -> None: ...
    def OnImageGrabbed(self, camera: InstantCamera, grabResult: GrabResult) -> None: ...
